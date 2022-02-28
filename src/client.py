from socket import *


class client:

	# constructor
	def __init__ (self, serverName, serverPort):
		self.serverName = serverName
		self.serverPort = serverPort


	# creating UDP socket
	def udpSocket(self):
		global clientSocket
		clientSocket = socket(AF_INET, SOCK_DGRAM)

	#print(serverPort)
	# sending a message to server
	def messages(self):
    		
		while True:    		
    		
				message = raw_input('input lowercase sentence\n')
				if message == "Exit":
					print("connection is closing...")
					clientSocket.close()
					print("connection is closed...")
					#lock.release()
					break
				clientSocket.sendto(message.encode(), (self.serverName, self.serverPort))
				self.receives()
				#print(self.serverPort)
	#receiving a message from a server
	def receives(self):
    		
			print("receiving....")
			modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

			#print("from server", end='')
			print("from server : ", modifiedMessage)
			print(serverAddress)
			#clientSocket.close()

def main():
	client1 = client('127.0.0.1', 40506)
	client1.udpSocket()
	client1.messages()
	client1.receives()
	#print(client1)

main()