from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")

msHis = {}
nameList = []
ipList = []


def receiver_addr(name):
    counter = 0
    for i in nameList:
        if i == name:
            return ipList[counter]
        counter += 1
        


def resendOld(receiverName):
    
    for i in msHis:
        if i == receiverName:
            print(f"address: {receiver_addr(receiverName)}")
            print(f"name: {receiverName}")
            # serverSocket.sendto(msHis[i], receiver_addr(receiverName))


while True:
    message, clients = serverSocket.recvfrom(2048)
   
    if message[0:1] == "L":
        
       # if nameList.index(message[2:]) == -1:
        if message[2:] in nameList:
            print("resend")
            resendOld(message[2:])
            # whatever function to prompt the guy to try a different name 
        
        else:
            nameList.append(message[2:])
            ipList.append(clients)
            # resendOld(message[2:])
        print(nameList)
        print(ipList)
        #else:
            #find a different name

    else:

         
 
        name = message[:message.index(":")]
        msHis[name] = message[message.index(":"):] 

        name = name.strip().split()
        message = message[message.index(":")  + 1:]


        for i in name:
        
            index = nameList.index(i)

            sendtoAddr = ipList[index]

            print(sendtoAddr)
            

            

            #print(message)

            serverSocket.sendto(message, sendtoAddr)
            print("sent...")




#serverSocket.sendto(modifiedMessage.encode(),clientAddress)    