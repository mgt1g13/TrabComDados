from bitstring import BitArray
from frameMaker import frameMaker
from frameDecoder import frameDecoder
import time
from ackMaker import ackMaker
from ackMaker import ackDecoder


class DataLinkSenderControl:
    def __init__(self, windowSize = 16, timeout = 5):
        self.buffer = []
        for i in range(windowSize):
            self.buffer.append((None, time.perf_counter()))
        self.endSentData = 0
        self.beginSentData = 0
        self.timeout = timeout
        self.framemaker = frameMaker()
        self.ackDecoder = ackDecoder()
        self.fileEnd = 0

    def getFrame(self):
        #itera para verificar timeout
        i = self.beginSentData % len(self.buffer)
        t1 = time.perf_counter()
        while(i != self.endSentData%len(self.buffer)):
            (frame, counter) = self.buffer[i]
            if((t1 - counter > self.timeout) and (frame != None)):
                self.buffer[i] = (frame, time.perf_counter())
                print("Sending frame " + str(i) + " Windown: " + str(self.beginSentData % len(self.buffer)) + ", " + str(self.endSentData%len(self.buffer)) )
                return frame
            i = (i+1)%(len(self.buffer))

        #Aloca frame novo
        if((self.endSentData - self.beginSentData) < len(self.buffer)-2):
            frame = self.framemaker.getFrame(self.endSentData%len(self.buffer))
            if (frame == None):
                self.fileEnd = 1
                return BitArray('0b1') #Retorna o frame '1' caso seja o fim do arquivo
            self.buffer[self.endSentData%len(self.buffer)] = (frame, time.perf_counter())
            self.endSentData = self.endSentData+1
            print("->Sending frame "  + str(self.endSentData%len(self.buffer) -1 ) + " Windown: " + str(self.beginSentData % len(self.buffer)) + ", " + str(self.endSentData%len(self.buffer)))
            return frame

        return None
        #retorna nada se tiver cheio o buffer e nao deu timeout (testar se o retorno for NONE)
        
    def validateAck(self, frame):
        frame = self.ackDecoder.decodeAck(frame)
        if(frame == None):
            return 0
        ackNumber = frame[8:].uint
        print("Ack Number: ", ackNumber)
        if(ackNumber > len(self.buffer)): #Caso o checsum falhe, mas mesmo assim o valor de ack seja absurdo
            return 0
        while (self.beginSentData%len(self.buffer) != ackNumber):
            self.beginSentData = self.beginSentData + 1
        if ((self.fileEnd == 1) and (self.beginSentData == self.endSentData)):
            return 1 #retorna 1 se já acabou o arquivo e recebeu o ultimo Ack

        return 0




from dataPrinter import dataPrinter
from ackMaker import ackMaker

class DataLinkReceiverControl:
    def __init__(self, windowSize = 16, rcId = 0, OUTfileName = 'dOut.txt'):
        self.buffer = []
        for i in range(windowSize):
            self.buffer.append((BitArray('0b0'), time.perf_counter()))
        self.expectedFrame = 0
        self.frameDec = frameDecoder()
        self.id = rcId
        self.dataPrinter = dataPrinter(OUTfileName)
        self.ackMaker = ackMaker()

        
    def receiveFrame(self, frame):
        if (frame.bin == '1'):
            return self.ackMaker.makeAck(self.expectedFrame)
        (controlData, frame) = self.frameDec.decodeFrame(frame)
        #print(controlData)
        #print(frame)
        if (controlData == None) or (frame == None):
            print("I am here")
            return self.ackMaker.makeAck(self.expectedFrame)
        
        destId = controlData[4:8].uint
        if (destId != self.id):
            print ("Destino invalido")
           # exit(101)

        frameLen = controlData[16:24]
        #faz algo com isso...

        frameNumber = controlData[8:16].uint
        #print("Received frame number: " +  str(frameNumber) + " expecting " + str(self.expectedFrame))
        if (frameNumber != self.expectedFrame):
            return self.ackMaker.makeAck(self.expectedFrame)

        print("Yay, got the frame I was expecting" + str(frameNumber))
        self.dataPrinter.printData(bytes.fromhex(frame.hex))
        self.expectedFrame = (frameNumber+1)%len(self.buffer)
        return self.ackMaker.makeAck(self.expectedFrame)


    def endSession(self):
        self.dataPrinter.closeFile()
