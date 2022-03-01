from socket import *


serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

name = raw_input("enter name ")
clientSocket.sendto(name.encode(), (serverName, serverPort))

while True:

    senders = raw_input("send to: ")
    message = raw_input("input lowercase sentence:")

    name = senders + ":"

    msg = name + message 
   # print(msg)

    clientSocket.sendto (msg.encode(),(serverName, serverPort))

    modifiedMessage, clients = clientSocket.recvfrom(2048)
    print(modifiedMessage)
    

#clientSocket.close()