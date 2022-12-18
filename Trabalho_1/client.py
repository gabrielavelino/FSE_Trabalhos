import socket
from time import sleep
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
        return CLIENTE

    def ligaTodosLed(self,sala):
        # GPIO.output(18, GPIO.HIGH)
        # GPIO.output(23, GPIO.HIGH)
        # GPIO.output(24, GPIO.HIGH)
        # GPIO.output(25, GPIO.HIGH)
        sala.manipulaLed(1,0)
        sala.manipulaLed(1,1)
        sala.manipulaLed(1,2)
        sala.manipulaLed(1,3)
    
    def desligaTodosLed(self,sala):
        sala.manipulaLed(0,0)
        sala.manipulaLed(0,1)
        sala.manipulaLed(0,2)
        sala.manipulaLed(0,3)

    def organizaDados(self,sala):
        msn = f'\nEstado Lampada: {sala.getEstadoLampada1()}\nEstado Lampada 2: {sala.getEstadoLampada2()}\nEstado Projetor: {sala.getEstadoProjetor()}\nEstado Ar condicionado: {sala.getEstadoArCondicionado()}\nEstado sensor fumaça: {sala.getEstadoSensorFumaca()}\nEstado sensor presença: {sala.getEstadoSensorPresenca()}\nEstado sensor porta: {sala.getEstadoSensorPorta()}\nEstado sensor janela: {sala.getEstadoSensorJanela()}\nEstado alarme sala: {sala.getEstadoAlarmeSala()}\n'
        # msn = [sala.getEstadoLampada1(), sala.getEstadoLampada2(), sala.getEstadoProjetor()]
        return msn

    
    def recebeDados(self,conexao,FORMAT,sala,GPIO):
        msg = (conexao.recv(2048).decode(FORMAT))
        print(f"msg: {msg}")
        
        if msg == '1':
            msn = self.organizaDados(sala)
            conexao.sendall(str.encode(msn))
        elif msg == '2':
            self.ligaTodosLed(sala)
            conexao.sendall(str.encode('Ligou todos os leds Sala 1'))
        elif msg == '3':
            self.desligaTodosLed(sala)
            conexao.sendall(str.encode('Desligou todos os leds Sala 1'))
        
    def enviaDados(self,msg,conexao):
        message = msg.encode()
        msg_length = len(message)
        send_length = str(msg_length).encode()
        send_length += b' ' * (self.HEADER - len(send_length))
        # conexao.send(send_length)
        conexao.send(message)

    
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
        
    
    

