import sys
from bitstring import BitArray


class dataPrinter:

    def __init__(self, fileName):
        self.outputDataFile = open(fileName, 'a+')
        print("Arquivo aberto, começando a escrever.")

    def printData(self, pData):
        self.outputDataFile.write(pData.to_bytes((pData.bit_length()+7)//8, 'big').decode())

    def closeFile(self):
        self.outputDataFile.close()
