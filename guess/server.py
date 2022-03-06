from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")

nameList = []
ipList = []


while True:
    message, clients = serverSocket.recvfrom(2048)
 
    if message[0:1] == "L":
        
       # if nameList.index(message[2:]) == -1:
        if message[2:] in nameList:
            pass 
            # whatever function to prompt the guy to try a different name 
        else:
            nameList.append(message[2:])
            ipList.append(clients)
        print(nameList)
        print(ipList)
        #else:
            #find a different name

    else:

        name = message[:message.index(":")]

        name = name.strip().split()

        for i in name:
        
            index = nameList.index(i)

            sendtoAddr = ipList[index]

            print(sendtoAddr)
            

            message = message[message.index(":")  + 1:]

            print(message)

            serverSocket.sendto(message, sendtoAddr)
            print("sent...")


        


   # serverSocket.sendto(modifiedMessage.encode(),clientAddress)