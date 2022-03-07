from socket import *

# import codecs


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

msgHistory = {}  # dictionary for storing all messages
nameList = []  # stores usernames
ipList = []  # store addresses

print("The server is ready to receive...")


def decrypt(message):
    decryptdData = ""
    data = name.split(",")
    data = data[:len(data)-1]

    for i in data:
        toInt = int(i)
        message = chr(toInt)
        decryptdData += message

    return decryptdData


# sends message history
def resendOld(receiverName):
    for name in msgHistory:
        if name == receiverName:
            index = nameList.index(receiverName)
            address = ipList[index]

            for i in msgHistory[receiverName]:
                serverSocket.sendto("HISTORY MESSAGES\n" + i.encode(), address)


while True:
    message, clients = serverSocket.recvfrom(2048)
    message = decrypt(message)

    message = message.decode()

    # a login message
    if message[0:1] == "L":

        # sends message history to client when they return to the chat
        if message[2:] in nameList:
            print("resend")
            index = nameList.index(message[2:])
            ipList[index] = clients
            resendOld(message[2:])

        # store client information on first login
        else:
            print(message[2:] + " is online")
            nameList.append(message[2:])
            ipList.append(clients)

            

    # a regular message
    else:
        
        name = message[:message.index(":")]

        name = name.strip().split()
        message = message[message.index(":") + 1:]

        for i in name:
            index = nameList.index(i)

            sendtoAddr = ipList[index]

            

            # finds username of the sender and concatenate it with the message they sent
            index2 = ipList.index(clients)
            sender_name = nameList[index2]
            store_msg = sender_name + ">" + message

            serverSocket.sendto(store_msg.encode(), sendtoAddr)
            print("sent...")



            # store messages in an array and add to the dictionary

            if i in msgHistory:
                grp = msgHistory[i]
                grp.append(store_msg)
            else:
                group = [store_msg]
                msgHistory[i] = group
