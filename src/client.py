from socket import *

class client:

	#clientSocket = 0

	# Constructor
	def __init__ (self, serverName, serverPort):
		self.serverName = serverName
		self.serverPort = serverPort


	# creating UDP socket
	def udpSocket(self):
		# making clientSocket global
		global clientSocket
		clientSocket = socket(AF_INET, SOCK_DGRAM)


	def messages(self):
    		
		while True:    		
    		
				message = raw_input('input lowercase sentence\n')
				if message == "Exit":
					print("connection is closing...")
					clientSocket.close()
					print("connection is closed...")
					break
				clientSocket.sendto(message.encode(), (self.serverName, self.serverPort))

				receivedMessage, serverAddr = clientSocket.recvfrom(2048)
				print (receivedMessage)
			#	print(self.serverPort)

	#This function is redundant don't delete it yet
	def receives(self):
		print("receiving....")
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

		#print("from server", end='')
		print("from server : ", modifiedMessage)
		
		#clientSocket.close()

def main():
	client1 = client('127.0.0.1', 40506)
	client1.udpSocket()
	client1.messages()
	#print(client1)

main()