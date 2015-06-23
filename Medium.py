from bitstring import BitArray
import socket
from random import randint
import signal
import sys



#######################################################################
#                        Sender                                       #
#######################################################################

senderPort = 5000
senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
senderSocket.bind(('', senderPort))
senderSocket.setblocking(0)

senderAckPort = senderPort + 1
senderAckSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



#######################################################################
#                       Receiver                                      #
#######################################################################

receiverPort = 6000
receiverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



receiverAckPort = receiverPort + 1
receiverAckSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiverAckSocket.bind(('', receiverAckPort))
receiverAckSocket.setblocking(0)

########################################################################

packageErrors = 0
packagesLost = 0
packagesReceived = 0
packagesPassed = 0

ackErrors = 0
ackLost = 0
ackReceived = 0
ackPassed = 0

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        f = open('log.txt', 'w')
        f.write("Pacotes totais: " + str(packagesReceived) + '\n')
        f.write("Pacotes enviados com erro: " + str(packageErrors) + '\n')
        f.write("Pacotes perdidos: " + str(packagesLost) + '\n')
        f.write("Pacotes enviados com sucesso: " + str(packagesPassed) + '\n')

        f.write("\n\nAcks totais: " + str(ackReceived) + '\n')
        f.write("Acks repassados com erro: " + str(ackErrors) + '\n')
        f.write("Acks perdidos: " + str(ackLost) + '\n')
        f.write("Acks transmitidos com sucesso: " + str(ackPassed) + '\n')

        f.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    try:
        dataFrame, client = senderSocket.recvfrom(4096)
        packagesReceived = packagesReceived +1
        send = randint(1, 100)
        if(send > 10):
            #print("I am here")
            packagesPassed = packagesPassed + 1
            receiverSocket.sendto(dataFrame, ('127.0.0.1', receiverPort))
        elif (send > 5):
            if(len(dataFrame) > 30):
                print("Added Error")
                packageErrors = packageErrors + 1
                temp = BitArray('0b' + dataFrame.decode('utf-8'))
                temp[10] = not temp[10]
                temp[11] = not temp[11]
                temp[15] = not temp[15]
                temp[12] = not temp[12]
                temp[23] = not temp[23]
                temp[27] = not temp[27]
                temp[30] = not temp[30]
                receiverSocket.sendto(bytes(temp.bin, 'utf-8'), ('127.0.0.1', receiverPort))
            else:
                packagesPassed = packagesPassed + 1
                receiverSocket.sendto(dataFrame, ('127.0.0.1', receiverPort))
        else:
            packagesLost = packagesLost + 1
            print("Lost package")
    except socket.error:
        None
    
    try:
        
        ackFrame, client = receiverAckSocket.recvfrom(1024)
        send = randint(1,100)
        ackReceived = ackReceived + 1
       
        if(send > 10):
            ackPassed = ackPassed + 1
            senderAckSocket.sendto(ackFrame, ('127.0.0.1', senderAckPort))
        elif (send > 5):
            print("Added Ack Error")
            temp = BitArray('0b' + ackFrame.decode('utf-8'))
            if(len(temp) > 9):
                temp[9] = not temp[9]
                ackErrors = ackErrors + 1
                senderAckSocket.sendto(bytes(temp.bin, 'utf-8'), ('127.0.0.1', senderAckPort))
            else:
                ackPassed = ackPassed + 1
                senderAckSocket.sendto(ackFrame, ('127.0.0.1', senderAckPort))
        else:
            ackLost = ackLost + 1
            print("Lost ACK")
       # i = i + 1
    except socket.error:
            None
    
        
    
    



