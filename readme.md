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