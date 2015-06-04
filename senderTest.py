import socket
from dataGenerator import dataGenerator
from bitstring import BitArray


class Sender:
    
    def __init__(self, host):
        self.dest = (host, 5000)
        __initSocket()

    def __init__(self, host, port):
        self.dest = (host, port)
        __initSocket()

    def __initSocket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def closeSocket(self):
        self._socket.close()

    def send(self, frame):
        self._socket.sendto(bytes(frame.bin, 'utf-8'), destino)
        
          

HOST = '127.0.0.1'
PORT = 5000
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (HOST, PORT)

file = "dados.txt"
dataGen = dataGenerator(file)

i=0
while i<50:
    frame = dataGen.getData()
    sender.sendto(bytes(frame.bin, 'utf-8'), destino)
    i = i+1
sender.close()
