import socket
import time
import sys
import threading

# HEADER = 128
# PORT = 10471
# HOST = sys.argv[-1]
# # SERVER = sys.argv[-1]
# # SERVER = "192.168.1.129"            ## 43
# # SERVER = "192.168.1.146"            ## 44
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "!DISCONNECT"
# # ADDR = (SERVER, PORT)
# ADDR = (HOST, PORT)
class cliente():
    def __init__(self,HEADER,PORT,HOST,ADDR):
        self.HEADER = HEADER
        self.PORT = PORT
        self.HOST = HOST
        self.ADDR = ADDR
    
    def iniciaConexao(self):
        CLIENTE = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        CLIENTE.connect(self.ADDR)
        CLIENTE.sendall(str.encode('Ola eu estou conectado...'))
        data = CLIENTE.recv(1024)
        print(data)
        return CLIENTE

    
    # def enviaDados(self):
    #     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #     client.connect(self.ADDR)
    #     client.sendall(str.encode('Ola eu estou conectado...'))
    #     data = client.recv(1024)
    #     print(data)
        # while True:
            
        #     print('mensagem ecoada: ', data.decode())
        #     time.sleep(2)
        #     print('mensagem ecoada: ', data.decode())
        #     time.sleep(2)
        #     num = int(input('Coloque uma entrada: '))
        #     client.sendall(str.encode('O numero recebido foi: '))
        #     client.sendall(str.encode(str(num)))
        #     print('Voce escolheu: 'f'{num}')
        #     if (num == 0):
        #         print('Fechando conexão...')
        #         break
        
    def send(self,msg,conexao):
        message = msg.encode()
        msg_length = len(message)
        send_length = str(msg_length).encode()
        send_length += b' ' * (self.HEADER - len(send_length))
        # conexao.send(send_length)
        conexao.send(message)
    
    

