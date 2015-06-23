#coding: utf-8

#Guilherme Gaiardo e Matheus Garay
#Classe que é responsavel por criar o frame.
#Vai chamar os métodos de outras classes que adicionam diversas partes do frame
#e estruturar em um frame enviavel pela camada fisica.
#Etapas:
#   0- Inicializar as classes que fazem parte da etapa de geração do frame
#   1- pegar N bytes de dados do dataGenerator.
#   2- adiconar a flag no inicio e no fim do frame
#   3- verificar se nao existem dados iguais a flag, se existir, colocar o marcador
#   4- adicionar o checksum
#   5- adicionar os dados de controle(idSender, idReceiver, nPacote)
#   6- retornar o frame completo a quem envia


from bitstring import BitArray
from dataGenerator import dataGenerator
from flagger import Flagger
from controlData import controlData
from checksum import Checksummer
from random import randint


class frameMaker:

    def __init__(self, frameSize = 128, INfileName = 'Carlos.jpg', flag = BitArray('0b00101110')): 
        self.dataGen = dataGenerator(INfileName, frameSize)
        self.checksummer = Checksummer()
        self.controlData = controlData(1, 0)
        self.flagger = Flagger(flag)
        

    def getFrame(self, frameNumber):
        frame = self.dataGen.getData()
        if (frame == ''):
            return None
        #print("Antes controle -> " + str(len(frame)))
        frame = self.controlData.addControlData(frame, frameNumber)
        #print("Depois controle -> " + str(len(frame)))
        frame = self.checksummer.addChecksum(frame)
        #print("Depois check -> " + str(len(frame)))
        frame = self.flagger.encode(frame)
        #checar se nao tem o marcador ou a flag no meio dos dados

        return frame


#fm = frameMaker()
#for x in range(0,10):
#    print(fm.getFrame().bin)
