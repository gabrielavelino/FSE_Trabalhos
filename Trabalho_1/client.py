import socket
import time
import sys
import threading

HEADER = 128
PORT = 10211
HOST = 'localhost'
# SERVER = sys.argv[-1]
# SERVER = "192.168.1.129"            ## 43
# SERVER = "192.168.1.146"            ## 44
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# ADDR = (SERVER, PORT)
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
client.sendall('Ola')