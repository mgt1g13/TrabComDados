import socket
from bitstring import BitArray
from frameDecoder import frameDecoder
from DataLinkControl import DataLinkReceiverControl

class Receiver:
    
    def __init__(self, host, source = '127.0.0.1', port = 6000):
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
        self._socket.settimeout(3)
        try:
            dataIn, client = self._socket.recvfrom(4096)
        except socket.timeout:
            return None
        return BitArray('0b'+dataIn.decode('utf-8'))

    def sendAck(self, frame):
        self._ackSocket.sendto(bytes(frame.bin, 'utf-8'), self.ackDest)




from time import sleep
from time import perf_counter
from random import randint


rec = Receiver('')
dc = DataLinkReceiverControl()
comeco = 1

x = 0
while True:
    nextFrame = rec.receive()
    if not nextFrame:
        if comeco == 1:
            continue
        break
    comeco = 0
    ack = dc.receiveFrame(nextFrame)
    if ack: #Se tiver ack para enviar (pode ter ocorrido erro na transmissão
        rec.sendAck(ack)
   # print("It: ", x)
    #x = x+1
    #sleep(0.01s)
dc.endSession()
rec.closeSocket()
