import socket 
import threading
import sys
import os
from time import sleep

HEADER = 128
PORT = 10472
HOST = sys.argv[-1]
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(ADDR)
server.listen()
print('Esperando a conexão do cliente...')

conn, ender = server.accept()

print("Conectado em", ender)

data = conn.recv(1024)
print(data.decode())

while True:
    print('\n######### SERVIDOR CENTRAL ##########')
    print('1 - Estados sensores\n')
    print('2 - Ligar Lampadas/Ar condicionado/Projetor\n')
    print('3 - Desligar Lampadas/Ar condicionado/Projetor\n')
    opcao = int(input('Digite sua opção: '))
    if (opcao == 1):
        conn.sendall(str.encode('1'))
        print(conn.recv(1024).decode())
    elif (opcao == 2):
        conn.sendall(str.encode('2'))
        print(conn.recv(1024).decode())
    elif (opcao == 3):
        conn.sendall(str.encode('3'))
        print(conn.recv(1024).decode())
    elif (opcao == 4):
        print("Recebi nada")
        conn.close()
        break
    