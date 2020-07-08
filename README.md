Requirement: Python3.x installed

Link download Python: https://www.python.org/downloads/

------------------------------------------------------------------------

*Setup:
1) Edit MyAddr, MyPass, ToAddr and UserName in "Run.py" before using

2) Press Win+R to open Run box, type "cmd" without quote and press Enter

3) Write this command to the command prompt:
		
		pip install pyinstaller 
4) After successfully installed pyinstaller, type 

		cd path
	which path is a folder contains "Run.py"
	
	For example, I put "Run.py" in a folder's name "PassCh" in C: --> the command will be:

		cd C:\PassCh
		
5) Type this command and wait until it's done: 

		pyinstaller --noconsole --onefile Run.py
		
6) After it's done, there'll be several folder, go to "dist" folder and copy the "Run.exe" to anywhere you want

7) To make it run without login to the user, run the follow command in the command prompt: 

		sc create PassChanger binPath="path"
	which path is the permernant path to the "Run.exe" file(Step 6)

8) Open Task Manager by pressing Win+R and type "taskmgr" without quote

9) Choose tab Services --> click on "Open Services" at the bottom of the box, it will open Services box

10) Look for item's name is PassChanger and double click on it

11) With regard to "Startup type", choose "Automatic" or "Automatic(Delayed Start)" --> Apply --> OK

------------------------------------------------------------------------

*Note: 
You can add user to admin group by this command:

	net localgroup groupname username /add
	
Ex: You want to add user's name is "nhtri" to "Administrators" group

	-> net localgroup Administrators nhtri /add
