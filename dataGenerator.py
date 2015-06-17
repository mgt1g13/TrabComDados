#Guilherme Gaiardo e Matheus Garay
#classe responsavel por extrair os dados de um .txt
#nBytes é o Numero (maximo) de Bytes que devem ser lidos em uma chamada a funçao getData

import sys
from bitstring import BitArray

class dataGenerator:

    
    def __init__(self, fileName, nBytes):
        try:
            file = open(fileName,'r')
        except IOError:
            print("Nao abriu o arquivo " + fileName)
            sys.exit(1)

        self.nBytes = nBytes
        self.inputDataFile = file
        print("Arquivo aberto com sucesso.")

    def getData(self):
        data = BitArray(bin(int.from_bytes(self.inputDataFile.read(self.nBytes).encode(), 'big')))
        #print (data.bin)
        return data



#file = "dados.txt"
#dataGen = dataGenerator(file)
#d = dataGen.getData()
#print (d.bin)
#c = int(d.bin,2)
#print (c.to_bytes((c.bit_length() + 7) // 8, 'big').decode())
