#Guilherme Gaiardo e Matheus Garay
#Classe responsavel por adicionar os dados de controle ao frame
#Dados de controle serão: IDsender(4bits), IDdestino(4bits), FrameNumber(1Byte)
#e frameLen(1Byte) (frameLen vai dizer quantos bits de dados o quadro tem)


from bitstring import BitArray


class controlData:

    def __init__(self, senderId, destId):
        self.senderId = self._formatId(bin(senderId))
        self.destId = self._formatId(bin(destId))



    def addControlData(self, frame, frameNumber):
        #controlData = self._addFrameLen(len(frame))
        controlData = self._addFrameNumber(bin(frameNumber))
        controlData.prepend(self.destId)
        controlData.prepend(self.senderId)

        frame.prepend(controlData)
        return frame


    def getControlData(self, frame):
        return frame[:16]
    

    def _addFrameLen(self, length):
        #frameLen = bin(length)
        ##len - 2 pois a funcao bin() retorna uma string do tipo '0b...', com dois dados nao uteis
        #i = len(frameLen) - 2
        ##laco para preencher com 0s ate ter 8 bits
        #while (i<8):
            #frameLen = '0b0' + frameLen[2:]
            #i = i + 1
        
        return self._completeNBits(BitArray(bin(length)), 16)#BitArray(frameLen)


    def _addFrameNumber(self, frameNumber):
        #i = len(frameNumber) - 2
        

        #while(i<8):
            #frameNumber = '0b0' + frameNumber[2:]
            #i = i + 1

        
        return self._completeNBits(BitArray(frameNumber), 8)#'0b' + BitArray(frameNumber).bin


    def _formatId(self, Id):
        #metodo para pegar a ID e transformar em um BitArray de tamanho 4 (uint)
        #i = len(Id)\

        #while(i<4):
            #Id = '0b0' + Id[2:]
            #i = i + 1
        return self._completeNBits(BitArray(Id), 4)#BitArray(Id)

    
    def _completeNBits(self, frame, n):
        if(not(len(frame) <= n)):
            print("EEEERRROOOO" + str(len(frame)) + " " + str(n))
            return frame
        frame.prepend((n-len(frame))*BitArray('0b0'))
        return frame 


#f = BitArray('0b101')
#print (f)
#c = controlData(1,2)
#f = c.addControlData(f, 5)
#print (f.bin)
#print (c.getControlData(f))
#print(f[24:].bin)
