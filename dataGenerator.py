import sys
from bitstring import BitArray

class dataGenerator:

    
    def __init__(self, fileName):
        try:
            file = open(fileName,'r')
        except IOError:
            print("Nao abriu o arquivo " + fileName)
            sys.exit(1)

        self.inputDataFile = file
        print("Arquivo aberto com sucesso.")

    def getData(self):
        data = BitArray(bin(int.from_bytes(self.inputDataFile.read(5).encode(), 'big')))
        #print (data.bin)
        return data



#file = "dados.txt"
#dataGen = dataGenerator(file)
#d = dataGen.getData()
#print (d.bin)
#c = int(d.bin,2)
#print (c.to_bytes((c.bit_length() + 7) // 8, 'big').decode())
