from bitstring import BitArray

class Flagger:

    def __init__(self, flag = BitArray('0b00101110')):
        self.flag = flag


    def encode(self, frame):
        frame.append(self.flag)
        frame.prepend(self.flag)
        return frame

    def decode(self, frame):
        if (frame.bin[:8] == self.flag.bin and frame.bin[len(frame.bin)-8:] == self.flag.bin):
            return BitArray("0b" + frame.bin[8:len(frame.bin)-8])
                            



#flagger = Flagger()
#a = BitArray('0b1')
#print(a)
#b = flagger.encode(a)
#print(b)
#print(flagger.decode(b))
