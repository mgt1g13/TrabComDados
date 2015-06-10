#Guilherme Gaiardo e Matheus Garay
#Classe responsavel por "desmontar" o frame e escrever no arquivo.
#Ela retorna o numero do ACK que deve ser enviado


from dataPrinter import dataPrinter
from flagger import Flagger
from bitstring import BitArray



class frameDecoder:


    def __init__(self, frameSize = 5, OUTfileName = 'dOut.txt', flag = BitArray('0b00101110')):
        self.nFrame = 0

        self.dataPrinter = dataPrinter(OUTfileName)
        self.flagger = Flagger(flag)
        

    def decodeFrame(self, frame):
        frame = self.flagger.decode(frame)
        data = int(frame.bin, 2)
        self.dataPrinter.printData(data)

        self.nFrame += 1
        return self.nFrame

    def endSession(self):
        self.dataPrinter.closeFile()
