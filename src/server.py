#######  
from socket import *
import threading


number = 0
serverPort = 40506
socketAddress = []

# Creating a UDP socket

serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(("", serverPort))
print("server started...")

def connectClient():
#print(clientAddress, " connected")
	print("client connected")
	while True:
		message, clientAddress = serverSocket.recvfrom(2048)

		modifiedMessage = message.decode().upper()
		print(modifiedMessage)
		serverSocket.sendto(modifiedMessage.encode(), clientAddress)
		print("message sent")

	serverSocket.close()

connectClient()
