from bitstring import BitArray
import re

class Flagger:

    def __init__(self, flag):
        self.flag = flag
        self.pattern = str(flag.bin[:int(len(flag.bin)/2)])
        self.bitStuffedPattern = self.pattern + "1"

    #Faz Bitstuffing e coloca as flags
    def encode(self, frame):
        frame = BitArray( "0b"+ re.sub("(" + self.pattern + ")", self.bitStuffedPattern, frame.bin)) 
        frame.append(self.flag)
        frame.prepend(self.flag)
        return frame

    #Remove a flag e os bits de bitstuffing
    def _decode(self, frame):
        if (frame.bin[:len(self.flag)] == self.flag.bin and frame.bin[len(frame.bin)-len(self.flag):] == self.flag.bin):
            return BitArray("0b" + re.sub(self.bitStuffedPattern, "(" + self.pattern + ")", frame.bin[len(self.flag):len(frame.bin)-len(self.flag)]))

    #Acha o começo e o fim do quadro        
    def decode(self, frame):
        iterator = re.finditer("(" + self.flag.bin + ")",  frame.bin)
        start = len(frame)
        end = 0
        if(iterator):
            for obj in iterator:
                if(obj.start() < start):
                    start = obj.start()
        buffer = ''
        j = 0
        for i in frame.bin:
            buffer += i
            j += 1
            if(len(buffer) < len(self.flag)):
                continue
            if(buffer[(len(buffer) - len(self.flag)):] == self.flag.bin):
                end = j

        
        if(start == len(frame) or start >= end):
            return None
        return self._decode(BitArray("0b" + frame.bin[start:end]))
        


#flagger = Flagger(BitArray("0b11"))
#a = BitArray('0b010')
#print(a)
#b = flagger.encode(a)
#print("0b" + b.bin)
#b.append(BitArray("0b0001000"))
#print(flagger.decode(b))

