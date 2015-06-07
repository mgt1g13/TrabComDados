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


class frameMaker:

    def __init__(self, frameSize = 5, INfileName = 'dados.txt', flag = BitArray('0b00101110'), senderId):
        
        self.dataGen = dataGenerator(INfileName, frameSize)
        self.flagger = Flagger(flag)
        #incializar classe do checksum e metadados

    def getFrame(self):
        frame = self.dataGen.getData()
        frame = self.flagger.encode(frame)
        #checar se nao tem o marcador ou a flag no meio dos dados
        #adicionar o checksum e metadados
        return frame
