from socket import *

serverName = '127.0.0.1' # IP adress of server
serverPort = 40506      # Port number

clientSocket = socket(AF_INET, SOCK_DGRAM) #Creating UDP socket


message = raw_input('input lowercase sentence:\n') #Taking message from client

# send the message to server
clientSocket.sendto(message.encode() , (serverName, serverPort))

#read the message from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()

