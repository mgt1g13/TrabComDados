#Guilherme Gaiardo e Matheus Garay
#classe responsavel por extrair os dados de um .txt
#nBytes é o Numero (maximo) de Bytes que devem ser lidos em uma chamada a funçao getData

import sys
from bitstring import BitArray
import codecs


class dataGenerator:

    
    def __init__(self, fileName, nBytes):
        try:
            file = open(fileName,'rb')
        except IOError:
            print("Nao abriu o arquivo " + fileName)
            sys.exit(1)

        self.nBytes = nBytes
        self.inputDataFile = file
        print("Arquivo aberto com sucesso.")

    def getData(self):
        data = BitArray(self.inputDataFile.read(self.nBytes))
        #print (data.bin)
        return data



#file = "Carlos.jpg"
#out = open('teste.jpg', 'wb')
#dataGen = dataGenerator(file, 1500)
#while True:
#    d = dataGen.getData()
#    print(d)
#    if(d == ''):
#        break 
#    d =  bytes.fromhex(d.hex)
   
#    out.write(d)
#out.close()
#print (d.bin)
#c = int(d.bin,2)
#print (c.to_bytes((c.bit_length() + 7) // 8, 'big').decode())
