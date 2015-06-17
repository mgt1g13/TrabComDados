#Guilherme Gaiardo e Matheus Garay
#Classe responsavel por "desmontar" o frame e escrever no arquivo.
#Ela retorna o numero do ACK que deve ser enviado


from dataPrinter import dataPrinter
from flagger import Flagger
from bitstring import BitArray
from controlData import controlData
from checksum import Checksummer



class frameDecoder:


    def __init__(self, frameSize = 5, flag = BitArray('0b00101110')):
        self.controlData = controlData(1, 0)
        self.checksummer = Checksummer()
        self.flagger = Flagger(flag)
        

    def decodeFrame(self, frame):
        #retira a flag
        frame = self.flagger.decode(frame)

        #checa e retira o checksum
        frame = self.checksummer.verifyChecksum(frame)
        #if (frame == -1):
        #    print("checksum detectou um erro")

        #separa os dados de controle
        controlData = self.controlData.getControlData(frame)
        frame = frame[24:]
        #print (frame.bin)

        
        return (controlData,frame)
