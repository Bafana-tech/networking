from socket import *

serverPort = 40506

# Creating a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# binding socket to local port number 405060
serverSocket.bind(("", serverPort))

print("server started...")

while True:
	# read UDP socket into message
	message, clientAddress = serverSocket.recvfrom(2048)

	modifiedMessage = message.decode().upper()

	# send upper case string back to this client
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)

