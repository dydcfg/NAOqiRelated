## NAOqi Developement Guideline ##

### Outline ###
- NAOqi OS
- Some Key Concepts Before Programming
- Python SDK
- C++ SDK


edit by Renkai Xiang

---
### NAOqi OS ###

1.	introduction
	>The Operating System of the robot.

	>It is a GNU/Linux distribution based on Gentoo.

	>It’s an embedded GNU/Linux distribution specifically developed to fit the Aldebaran robot needs.

	>It provides and runs numbers of programs and libraries, among these, all the required one by NAOqi, the piece of software giving life to the robot.

2.	Accounts
	>The main user is nao, and like any GNU/Linux system, there is the super-user root.

	>By default, passwords are usernames. So, changing user to root using the su command will request the password root

	>**Logging in as root over ssh is now disabled.** However the su command remains available.

	>We recommend to change the nao‘s password using the web page.
	
	Below is the default accounts:

		User	Password 	Description
		nao		nao			default account
		root	root		administrator account


3.	How to access to it
	
	Simply accessing NAO over ssh.In a **Linux** terminal,run:
		
		$ ssh nao@192.168.1.10
	If using Windows, we need a terminal application, PuTTy for example.

### Key Concepts ###

1.	 What is NAOqi Framework
	>NAOqi is the name of the main software that runs on the robot and controls it.

	>The NAOqi Framework is the programming framework used to program Aldebaran robots.

	>It answers to common robotics needs including: parallelism, resources, synchronization, events.
2.	Cross platform
	
	It is possible to develop with NAOqi framework on Windows, Linux or Mac.

	-	Using Python: you will be able to easily run your code both on your computer or directly on the robot.

	-	Using C++: as it is a compiled language, you will need to compile your code for the targeted Operating System. So if you want to run C++ code on the robot, you will need to use a cross-compilation tool in order to generate a code able to run on the robot Operating System: NAOqi OS.
3.	The NAOqi process
	>The NAOqi executable which runs on the robot is a broker. When it starts, it loads a preferences file called autoload.ini that defines which libraries it should load. Each library contains one or more modules that use the broker to advertise their methods.

	*	Broker:
	>A broker is an object that provides:
	>Directory services: allowing you to find modules and methods.
	Network access: allowing the methods of attached modules to be called from outside the process.
	Most of the time, you don’t need to think about brokers. They do their work transparently, allowing you to write code that will be the same for calls to “local modules” (in the same process) or “remote modules” (in another process or on another machine).
	
	*	Proxy:
	>A proxy is an object that will behave as the module it represents.

	>For instance, if you create a proxy to the ALMotion module, you will get an object containing all the ALMotion methods.

	>To create a proxy to a module, (and thus calling the methods of a module) you have two choices:

	>Simply use the name of the module. In this case, the code you are running and the module to which you want to connect to must be in the same broker. This is called a local call.
	Use the name of the module, and the IP and port of a broker. In this case, the module must be in the corresponding broker.
4.	Modules
	>Typically each Module is a class within a library. When the library is loaded from the autoload.ini, it will automatically instantiate the module class.

	>In the constructor of a class that derives from ALModule, you can “bind” methods. This advertises their names and method signatures to the broker so that they become available to others.
	*	Local modules:
		*	Local modules are two (or more) modules launched in the same process. They speak to each other using only ONE broker.
	*	Remote modules:
		*	Remote modules are modules which communicate using the network. A remote module needs a broker to speak to other modules. The broker is responsible for all the networking part. 
	*	Broker to Broker connection:
		*	You can connect two modules together by connecting their brokers.

		*	For example, you have two modules B and C. When you connect their brokers, B can access to C’s functions and C can access to B’s functions.

		*	To connect modules this way you need to specify the IP address and port number of the main broker. (--pip, --pport command line option when you start your module). Then you can access the module by getting a proxy on it:

				AL::ALProxy proxy = AL::ALProxy(<modulename>);
		
			Since module’s broker is already connected using --pip and --pport, you do not need to specify IP address and port number when you create a proxy.
	*	Proxy to Broker connection
		*	You can connect your module to another one without specifying --pip and --pport. To do that, you need to create a proxy inside your module and connect it to the broker IP address and port number you want.
		*	For example, you have two modules B and C. When you connect B to C just using a proxy, B can access to C functions BUT C cannot access to B functions.
		
				// A broker needs a name, an IP and a port to listen:
				const std::string brokerName = "mybroker";
				// NAOqi ip
				const std::string pip = "127.0.0.1"; // local NAOqi
				// NAOqi port
				int pport = 9559;

				// Create your own broker
				boost::shared_ptr<AL::ALBroker> broker =
  				AL::ALBroker::createBroker(brokerName, "0.0.0.0", 54000, pip, pport);
				AL::ALProxy proxy = AL::ALProxy(broker, <modulename>);
5.	Blocking and non-blocking calls
	*	Blocking calls:
		*	The next instruction will be executed after the end of the previous call. All calls can raise an exception and should be encapsulated in a try-catch block. Calls can have return values.
			
				std::string status;
				status = module.doSomething();
				std::cout<<status<<std::endl;
	*	Non-blocking calls:
		*	By using the post object of a proxy, a task is created in a parallel thread. This enables you to do other work at the same time (e.g. walking while talking). Each post call generates a task id. You can use this task id to check if a task is running, or wait until the task is finished.
		
				int taskID;
				taskID = module.post.doSomething();
				std::cout<<taskID<<std::endl;
				//do things in parallel
6.	Reacting to events
	>A few modules expose also some events.

	>You must subscribe to event from an other module, using a callback that must be a method of your subscriber.

	>For instance, you can have a module called FaceReaction containing a method onFaceDetected.

	>You can subscribe the FaceReaction module to the FaceDetected method of the ALFaceRecognition module with the onFaceDetected callback.

	>This will cause the face detection algorithm to run, and every time a face is detected, the onFaceDetected callback will be called.

7.	The sensors, vision and audio values

	NAO provides 3 kinds of sensors values as well as vision values.
	
	All their values are stored in `ALMemory` and it's easy to get values from `ALMemory` in Python.

	**Sensors**
	1.	FSR values - Foot Force Sensor Values
	2.	Inertial Sensor values - Gyrometers Values/	Accelerometers Values/Torso Angle in radian
	3.	Sonar values

	**Vision**
	1.	Retrieving images
	2.	Video recording
	3.	Face detection and tracking
	4.	Vision recognition
	5.	Landmark detection
	
	**Audio**
	1.	AudioRecorder/AudioPlayer
	2.	TextToSpeech
	3.	SoundLocalization
	4.	VoiceEmotionAnalysis
