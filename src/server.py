#######  
from socket import *
import threading


number = 0
serverPort = 40506
socketAddress = []
messages = []




# Creating a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(("", serverPort))
print("server started...")

def connectClient():

	
	while True:
		#print("client connected")
		message, clientAddress = serverSocket.recvfrom(2048)
		print("client connencted")

		socketAddress.append(clientAddress)
		print("connected : ", clientAddress)
		

		modified = message.capitalize().decode()
		messages.append(modified)

		numsock = len(socketAddress)
		print(socketAddress)
		for i in range(0,numsock):
			if len(socketAddress) >= 1:
					serverSocket.sendto(modified.encode(), clientAddress)
			
			else:
					serverSocket.sendto(messages[len(socketAddress)-i].encode(), socketAddress[i])

					#serverSocket.sendto(messages[len(socketAddress)-i].encode(), socketAddress[i])	
				

		if message == "exit":
				break
	#	modifiedMessage = message.decode().upper()
	#	print("connected %s" % str(clientAddress))
	#	serverSocket.sendto(modifiedMessage.encode(), clientAddress)


	#serverSocket.close()

connectClient()
