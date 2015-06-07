import socket
from dataGenerator import dataGenerator
from bitstring import BitArray
from frameMaker import frameMaker

class Sender:
    
    def __init__(self, host, port):
        self.dest = (host, port)
        self.__initSocket()

    def __initSocket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def closeSocket(self):
        self._socket.close()

    def send(self, frame):
        self._socket.sendto(bytes(frame.bin, 'utf-8'), self.dest)
        
          

HOST = '127.0.0.1'
PORT = 5000

sender = Sender(HOST, PORT)
frame = frameMaker()

for i in range(0,49):
    sender.send(frame.getFrame())
    
sender.closeSocket()
