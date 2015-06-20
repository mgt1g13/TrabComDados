#Guilherme Gaiardo e Metheus Garay
#Classe responsavel por fazer um frame de ACK
#deve conter o senderId, o recieverId e 8 bits para dizer o numero do ACK

from bitstring import BitArray


class ackMaker:

    def __init__(self, senderId = 1, receiverId = 0):
        self.senderId = self._completeNBits(BitArray(bin(senderId)), 4)
        self.receiverId = self._completeNBits(BitArray(bin(receiverId)), 4)


    def makeAck(self, expectedFrame):
        ack = self._completeNBits(BitArray(bin(expectedFrame)), 8)
        ack.prepend(self.receiverId)
        ack.prepend(self.senderId)
        #print("Ack Binary: ", ack.bin)
        return ack

        
    def _completeNBits(self, frame, n):
        if(not(len(frame) <= n)):
            print("erroooo")
            exit(201)
        frame.prepend((n-len(frame))*BitArray('0b0'))
        return frame
