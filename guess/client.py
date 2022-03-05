from socket import *
import struct
import threading
import time
import zlib     # For checking checksum
import codecs



serverName = gethostname()
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

print("-------------------WELCOME TO CHAT APP----------------------")
udpHeader = ""

name = raw_input("enter name ")
clientSocket.sendto(name, (serverName, serverPort))



def send():  
    # Making name to be as lowercase
    while True:
        
        typeOfChat = raw_input("1 for Broadcast or 2 for one person chat ")

        if typeOfChat == "2":
            while True:

                senders = raw_input("send to or press Exit to leave  >> ")
                if senders.lower() == "exit":
                    break
                
                name = senders + ":"
                message = raw_input("message >>")

                msg = name + message
                msg = msg.encode()

                # dealing with data corruption before sending the data
                packet_length = len(message)
                checktotal = checksum(message)
                print(checktotal)
                #we dont know the destination port before we send so we make it static
                udpHeader = struct.pack("ffff", serverPort,101, packet_length,checktotal)
                headerMsg = msg + udpHeader
                
                clientSocket.sendto (headerMsg,(serverName, serverPort))   
               # print("Message sent!")

        elif typeOfChat == "1":

            while True:

    
                senders = raw_input("send to or press Exit to leave  >> ")
                if senders.lower() == "exit":
                    break
                
                name = senders + ":"
                message = raw_input("message >>")

                msg = name + message
                msg = msg.encode()

                # dealing with data corruption before sending the data
                packet_length = len(message)
                checktotal = checksum(message)
                print(checktotal)
                #we dont know the destination port before we send so we make it static
                udpHeader = struct.pack("ffff", serverPort,12000, packet_length,checktotal)
                headerMsg = msg + udpHeader
                
                clientSocket.sendto (headerMsg,(serverName, serverPort))   
                print("Message sent!")

       # else:



def receive():
    
    while True:
        print("Recieving Or Sending ..........................................")
        modifiedMessage, clients = clientSocket.recvfrom(2048)
       # print("RECEIVED ", modifiedMessage)

        udpHeadMessage = modifiedMessage[len(modifiedMessage) -16 :]
        data = modifiedMessage[:len(modifiedMessage) - 16]
        data = data.decode()

        udpunpackMessage = struct.unpack("ffff", udpHeadMessage)
       # print(udpunpackMessage)


        receivedMessageCheckSum = checksum(data)
       # print(receivedMessageCheckSum)
        sentCheckSum = udpunpackMessage[3]
       

        if receivedMessageCheckSum == sentCheckSum:

        # print(modifiedMessage[:len(modifiedMessage) - 16])

                print(modifiedMessage)

        else:
                print("WARNING DATA WAS LOST")
               # print("Sent ", int(sentCheckSum))
                print("Received ", int(receivedMessageCheckSum))
                print(data)
                print(sentCheckSum)

def checksum(messageSent):
    checksum = zlib.crc32(messageSent)
    return checksum

if __name__ == "__main__":

    t1 = threading.Thread(target=send)

    t2 = threading.Thread(target=receive)


    t1.start()
    t2.start()





