import socket
from bitstring import BitArray
from frameDecoder import frameDecoder
from DataLinkControl import DataLinkReceiverControl

class Receiver:
    
    def __init__(self, host, source = '127.0.0.1', port = 5000):
        self.origem = (host, port)
        self.ackDest = (source, (port+1))
        self.__initSocket()

    def __initSocket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(self.origem)
        self._ackSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def closeSocket(self):
        self._socket.close()
        self._ackSocket.close()

    def receive(self):
        dataIn, client = self._socket.recvfrom(1024)
        return BitArray('0b'+dataIn.decode('utf-8'))

    def sendAck(self, frame):
        self._ackSocket.sendto(bytes(frame.bin, 'utf-8'), self.ackDest)






rec = Receiver('')
dc = DataLinkReceiverControl()

x = 0
while True:
    nextFrame = rec.receive()
    if nextFrame.bin == '0':
        break
    rec.sendAck(dc.receiveFrame(nextFrame))
    print("It: ", x)
    x = x+1
dc.endSession()
rec.closeSocket()
