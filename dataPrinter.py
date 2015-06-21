import sys
from bitstring import BitArray


class dataPrinter:

    def __init__(self, fileName):
        self.outputDataFile = open(fileName, 'ab+')
        print("Arquivo aberto, começando a escrever.")

    def printData(self, pData):
        self.outputDataFile.write(pData)

    def closeFile(self):
        self.outputDataFile.close()
