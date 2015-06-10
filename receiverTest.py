import socket
from bitstring import BitArray
from frameDecoder import frameDecoder

class Receiver:
    
    def __init__(self, host, port = 5000):
        self.origem = (host, port)
        self.__initSocket()

    def __initSocket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(self.origem)

    def closeSocket(self):
        self._socket.close()

    def receive(self):
        dataIn, cliente = self._socket.recvfrom(1024)
        return BitArray('0b'+dataIn.decode('utf-8'))



rec = Receiver('')
decoder = frameDecoder()

for x in range(0,49):
    decoder.decodeFrame(rec.receive())
    
decoder.endSession()
rec.closeSocket()
