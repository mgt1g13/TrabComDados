#Guilherme Gaiardo e Metheus Garay
#Classe responsavel por fazer um frame de ACK
#deve conter o senderId, o recieverId e 8 bits para dizer o numero do ACK

from bitstring import BitArray
from checksum import Checksummer
from flagger import Flagger

def _completeNBits(frame, n):
    if(not(len(frame) <= n)):
        print("erroooo")
        exit(201)
    frame.prepend((n-len(frame))*BitArray('0b0'))
    return frame


class ackMaker:

    def __init__(self, senderId = 1, receiverId = 0, flag = BitArray('0b00101110')):
        self.senderId = _completeNBits(BitArray(bin(senderId)), 4)
        self.receiverId = _completeNBits(BitArray(bin(receiverId)), 4)
        self.flagger = Flagger(flag)
        self.checksummer = Checksummer()


    def makeAck(self, expectedFrame):
        ack = _completeNBits(BitArray(bin(expectedFrame)), 8)
        ack.prepend(self.receiverId)
        ack.prepend(self.senderId)
        ack = self.checksummer.addChecksum(ack)
        ack = self.flagger.encode(ack)
        #print("Ack Binary: ", ack.bin)
        return ack


class ackDecoder:
    def __init__(self, senderId = 1, receiverId = 0, flag = BitArray('0b00101110')):
        self.senderId = _completeNBits(BitArray(bin(senderId)), 4)
        self.receiverId = _completeNBits(BitArray(bin(receiverId)), 4)
        self.flagger = Flagger(flag)
        self.checksummer = Checksummer()

    def decodeAck(self, ack):
        ack = self.flagger.decode(ack)
        if(not ack):
            return None

        ack = self.checksummer.verifyChecksum(ack)
        if(not ack):
            print("Checksum detectou problema no ack") 
            return None

        return ack
    
    
