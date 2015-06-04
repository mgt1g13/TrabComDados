import socket
from bitstring import BitArray

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


##
##HOST = ''
##PORT = 5000
##receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##origem = (HOST, PORT)
##receiver.bind(origem)

rec = Receiver('')

while True:
##    dataIn, cliente = receiver.recvfrom(1024)
##    frame = BitArray('0b'+dataIn.decode('utf-8'))
    msg = int(rec.receive().bin,2)
    print (msg.to_bytes((msg.bit_length() + 7) // 8, 'big').decode())
rec.closeSocket
