#Guilherme Gaiardo e Matheus Garay
#Classe responsavel por adicionar, verificar e remover o checksum  do frame

from bitstring import BitArray

class Checksummer:

    def __init__(self, checksumSize = 8):
        self.checksumSize = checksumSize
        return

    def addChecksum(self, frame):
        frame.append(self._calculateChecksum(frame))
        return frame

    #Retorna o quadro sem o checksum se ele está correto
    #Caso contrário retorna -1
    def verifyChecksum(self, frame):
        checksumGiven = frame[(len(frame) - self.checksumSize):]
        data = frame[:(len(frame) - self.checksumSize)]
        checksumCalculated = self._calculateChecksum(data)

        if(checksumGiven == checksumCalculated):
            return data
        else:
            return None
        
            
    def _calculateChecksum(self, data):
        i = 0
        checksum = self.checksumSize*BitArray('0b0') #checksumSize bits 0
        #Vai pegando de 8 em 8 bits e fazendo o xor para calcular o checksum
        while(i < len(data)):
            if(len(checksum) == len(data[i:i+self.checksumSize])): 
                checksum = checksum ^ data[i:i+self.checksumSize]
            else:
                #Coloca 0s no que sobrou do quadro para calcular o checksum
                temp = data[i:i+self.checksumSize]
                temp.prepend((len(checksum)-len(data[i:i+self.checksumSize]))*BitArray('0b0'))
                checksum = checksum ^ (temp)
            i = i + self.checksumSize
        return checksum


#c = Checksummer()
#a = BitArray('0b00110010011')
#c.addChecksum(a)
#print(c.verifyChecksum(a).bin)
