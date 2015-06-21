import socket
from DataLinkControl import DataLinkSenderControl
from bitstring import BitArray
from frameMaker import frameMaker
from random import randint
from time import sleep


class Sender:
    
    def __init__(self, host = '127.0.0.1', port = 6000):
        self.dest = (host, port)
        self.ackSrc = ('', (port+1))
        self.__initSocket()

    def __initSocket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._ackSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._ackSocket.bind(self.ackSrc)
        self._ackSocket.setblocking(0)

    def closeSocket(self):
        self._socket.close()
        self._ackSocket.close()

    def send(self, frame):
        self._socket.sendto(bytes(frame.bin, 'utf-8'), self.dest)

    def receiveAck(self):
        try:
            ackFrame, client = self._ackSocket.recvfrom(1024)
        except socket.error:
            return None
        else:
            ack = BitArray('0b' + ackFrame.decode('utf-8'))
            #print ("Ack bin: ", ack.bin)
            return ack
        

from copy import copy        

HOST = '127.0.0.1'
PORT = 5000

sender = Sender(HOST, PORT)
dc = DataLinkSenderControl(timeout = 0.1)

x = 0
while True:
    ack = sender.receiveAck()
    if ack != None:
        if dc.validateAck(ack) == 1:
            sender.send(BitArray('0b0'))
            break
    nextFrame = dc.getFrame()
    if nextFrame != None:
        sender.send(nextFrame)
    #print("")
    #print ("It: ", x)
    x = x+1
    #sleep(2)
sender.closeSocket()
