import socket 
import threading
import sys
import os

HEADER = 128
PORT = 10211
# SERVER = sys.argv[-1]
HOST = 'localhost'
# SERVER = "192.168.1.129"            ## 43
# SERVER = "192.168.1.146"            ## 44
# ADDR = (SERVER, PORT)
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(ADDR)
server.listen()
print('Esperando a conexão do cliente...')

conn, ender = server.accept()

print("Conectado em", ender)

while True:
    data = conn.recv(1024)
    if not data:
        print("Fechando conexão...")
        conn.close()
        break
    else:
        conn.sendall(data)