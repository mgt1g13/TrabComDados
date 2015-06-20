#Guilherme Gaiardo e Matheus Garay
#Classe responsavel por "desmontar" o frame.
#Ela retorna os dados e os dados de controle separadamente


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
        FrameBuffer = frame
        #retira a flag
        frame = self.flagger.decode(frame)
        
        #checa e retira o checksum
        frame = self.checksummer.verifyChecksum(frame)
        if (not frame):
            print("checksum detectou um erro")
            return (None, None)

        #separa os dados de controle
        controlData = self.controlData.getControlData(frame)
        frame = frame[24:]
        #print (frame.bin)

        
        return (controlData,frame)
