import sys
from socket import *
import struct
import threading
import time
import zlib  # For checking checksum
import codecs

serverName = gethostname()  # IP address
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  #


def welcome():
    print("-----------------------WELCOME TO CHAT APP-------------------------")
    # user login by entering:
    # L <their username>
    name = input("Enter your username: ")
    clientSocket.sendto(name.encode(), (serverName, serverPort))


welcome()


def send():
    while True:

        typeOfChat = input("Enter <1> for Broadcast or <2> for one-to-one chat: ")

        if typeOfChat == "2":
            while True:

                senders = input("Enter username(of receiver) or press Exit to leave  >> ")
                if senders.lower() == "exit":
                    break

                name = senders + ":"
                message = input("message >>")

                msg = name + message
                msg = msg.encode()

                clientSocket.sendto(msg, (serverName, serverPort))
                print("Message sent!")  # codecs.encode(s, 'utf-8')

        elif typeOfChat == "1":

            senders = input("Enter usernames(of all receivers) or press Exit to leave  >> ")
            if senders.lower() == "exit":
                break

            name = senders + ":"
            message = input("message >>")

            msg = name + message
            msg = msg.encode()

            clientSocket.sendto(msg, (serverName, serverPort))
            print("Message sent!")


# To break out of the receiving state enter the username of the person you want to send a message to
def receive():
    while True:
        print()
        print("Wait to receive or send..........................................")
        recv_msg = clientSocket.recvfrom(2048)
        print(recv_msg)


def checksum(messageSent):
    checksum = zlib.crc32(messageSent)
    return checksum


if __name__ == "__main__":
    t1 = threading.Thread(target=send)

    t2 = threading.Thread(target=receive)

    t1.start()
    t2.start()
