__author__ = 'v-rexian'

import sys
import time
import socket
import Image
import io


from naoqi import ALProxy
import vision_definitions
from naoqi import ALBroker
from naoqi import ALModule

NAO_IP   = "nao.local"
NAO_PORT = 9559

class MyDataClass:
    def __init__(self):
        self.type = 0
        self.stringData = ''
        self.imageData  = Image()

class MyAgent:

    def __init__(self,serverIp,serverPort):
         self.serverIp   = serverIp
         self.serverPort = serverPort

    def textToSpeech(self, *_args):
        self.tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
        # Depends on what server returns
        self.tts.setLanguage(_args[0])
        self.tts.say(_args[1])

    def getResultFromServer(self, *_args):
        skt = socket.socket()
        skt.connect((self.serverIp, self.serverPort))

        if (_args[0] == 0):
            for i in range(0, len(_args[1])):
                _args[1][i].save("tmpImage.png", "PNG")
                inputFile = open("tmpImage.png", "rb")
                tmp = inputFile.read()
                skt.sendall(tmp)
                result = skt.recv(2048)
                print("%s\n", result)


    def getImage(self, *_args):
        '''

        :param _args: _args[0] - Number of images that required
        :return: - Array of images.

        '''
        camProxy   = ALProxy("ALVideoDevice", NAO_IP, NAO_PORT)
        resolution = vision_definitions.kQQVGA
        colorSpace = vision_definitions.kYUVColorSpace
        fps        = 20
        nameId     = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
        retImages  = []

        for i in range(0, _args[0]):
            print "getting image " + str(i)
            naoImage = camProxy.getImageRemote(nameId)
            # Get the image size and pixel array.
            imageWidth = naoImage[0]
            imageHeight = naoImage[1]
            array = naoImage[6]
            retImages.append(Image.frombytes("RGB", (imageWidth, imageHeight)))
            time.sleep(0.05)
        camProxy.unsubscribe(nameId)
        return retImages


def main():
    t = MyAgent('10.172.98.119', 13000)
    t.getResultFromServer()

if __name__ ==  "__main__":
    main()


