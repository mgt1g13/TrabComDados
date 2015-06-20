from bitstring import BitArray
import socket
from random import randint



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

while True:
    try:
        dataFrame, client = senderSocket.recvfrom(1024)
        send = randint(1, 100)
        if(send > 20):
            receiverSocket.sendto(dataFrame, ('127.0.0.1', receiverPort))
        elif (send > 10):
            if(len(dataFrame) > 30):
                print("Added Error")
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
                receiverSocket.sendto(dataFrame, ('127.0.0.1', receiverPort))
        else:
            print("Lost package")
    except socket.error:
            None
    
    try:
        
        ackFrame, client = receiverAckSocket.recvfrom(1024)
        send = randint(1,100)
        if(send > 20):
            senderAckSocket.sendto(ackFrame, ('127.0.0.1', senderAckPort))
        else:
            print("Lost ACK")
    except socket.error:
            None
    
        
    
    



