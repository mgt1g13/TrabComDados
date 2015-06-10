#Guilherme Gaiardo e Matheus Garay
#Classe responsavel por "desmontar" o frame e escrever no arquivo.
#Ela retorna o numero do ACK que deve ser enviado


from dataPrinter import dataPrinter
from flagger import Flagger
from bitstring import BitArray
from controlData import controlData
from checksum import Checksummer



class frameDecoder:


    def __init__(self, frameSize = 5, OUTfileName = 'dOut.txt', flag = BitArray('0b00101110')):
        self.dataPrinter = dataPrinter(OUTfileName)
        self.controlData = controlData(1, 0)
        self.checksummer = Checksummer()
        self.flagger = Flagger(flag)
        self.nFrame = 0
        

    def decodeFrame(self, frame):
        #retira a flag
        frame = self.flagger.decode(frame)

        #checa e retira o checksum
        frame = self.checksummer.verifyChecksum(frame)
        #if (frame == -1):
        #    print("checksum detectou um erro")

        #retorna os dados de controle
        controlData = self.controlData.getControlData(frame)
        #trata os dados de controle
        
        frame = frame[20:]
        print (frame.bin)
        data = int(frame.bin, 2)
        self.dataPrinter.printData(data)

        self.nFrame += 1
        return self.nFrame

    def endSession(self):
        self.dataPrinter.closeFile()
