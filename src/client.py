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
		message = raw_input('input lowercase sentence\n')

		clientSocket.sendto(message.encode(), (self.serverName, self.serverPort))
		print(self.serverPort)

	def receives(self):
		print("receiving....")
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

		#print("from server", end='')
		print(modifiedMessage)
		
		#clientSocket.close()

def main():
	client1 = client('127.0.0.1', 40506)
	client1.udpSocket()
	client1.messages()
	client1.receives()
	#print(client1)

main()