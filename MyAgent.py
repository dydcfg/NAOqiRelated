__author__ = 'v-rexian'

import sys
import time
import socket
import Image
import io


from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

class MyDataClass:
    type = 0
    stringData = ''


class MyAgent:
    def __init__(self,serverIp,serverPort):
         self.serverIp   = serverIp
         self.serverPort = serverPort

    def getResultFromServer(self, *_args):
        skt = socket.socket()
        skt.connect((self.serverIp,self.serverPort))
        inputFile = open("broker-libraries-modules.png","rb")
        tmp = inputFile.read()
        skt.sendall(tmp)
        result = skt.recv(1024)
        print("%s\n",result)

    def getImage(self, *_args):
        if (_args[0] == 0):
            return _args[0]
        return _args[0]

    #def getAudio(self, *_args):

def main():
    t = MyAgent('10.172.98.119',13000)
    t.getResultFromServer()

if __name__ ==  "__main__":
    main()


