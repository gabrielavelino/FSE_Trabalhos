from Sala import Sala
from time import sleep
import RPi.GPIO as GPIO
import board
import adafruit_dht
import sys
from client import cliente
import threading

## SERVIDOR DISTRIBUIDO ###
HEADER = 128
PORT = 10472
HOST = sys.argv[-1]
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (HOST, PORT)


# INICIALIZA SALA
client1 = cliente(HEADER,PORT,HOST,ADDR)
conexao = client1.iniciaConexao()

sala1 = Sala(7, 1, 12, 16, 20, 21, 26)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup([18,23,24,25,8],GPIO.OUT)
dhtDevice = adafruit_dht.DHT22(board.D4)
GPIO.setup([sala1.sensor_fumaca,sala1.sensor_janela,sala1.sensor_porta,sala1.sensor_presenca,sala1.sensorContagemPessoasEntrada,sala1.sensorContagemPessoasSaida],GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(sala1.sensor_fumaca, GPIO.BOTH, callback=sala1.sensorFumaca,bouncetime = 300)
GPIO.add_event_detect(sala1.sensor_janela, GPIO.BOTH, callback=sala1.sensorJanela,bouncetime = 300)
GPIO.add_event_detect(sala1.sensor_porta, GPIO.BOTH, callback=sala1.sensorPorta,bouncetime = 300)
GPIO.add_event_detect(sala1.sensor_presenca, GPIO.BOTH, callback=sala1.sensorPresenca,bouncetime = 300)
GPIO.add_event_detect(sala1.sensorContagemPessoasEntrada, GPIO.RISING, callback=sala1.sensorEntradaPessoas,bouncetime = 300)
GPIO.add_event_detect(sala1.sensorContagemPessoasSaida, GPIO.RISING, callback=sala1.sensorSaidaPessoas,bouncetime = 300)



def menu():
    print('Número de pessoa na sala: ', sala1.getEstadoSensorPessoasEntrada())
    print('\n######### Sala automatiza ##########\n')
    print('1 - Ligar lampadas - projetor - ar condicionado')
    print('2 - Desligar lampada')
    print('3 - Estados em tempo real')
    print('4 - Ligar alarme (somente quando não tem ninguém na sala!)')
    client1.recebeDados(conexao,FORMAT,sala1,GPIO)
    opcao = int(input('Digite sua opcao: '))

    if(opcao == 1):
        print('\n\n----------- Lista de comandos -------------\n')
        print('Lampada 1 da sala: digite 0\n')
        print('Lampada 2 da sala: digite 1\n')
        print('Arcondicionado: digite 2\n')
        print('Projetor multimídia: digite 3\n')
        print('Alarme: digite 4\n')
        escolheLed = int(input('Digite qual LED quer acender: '))
        sala1.manipulaLed(1,escolheLed)
        
    elif(opcao == 2):
            print('\n\n----------- Lista de comandos -------------\n')
            print('Lampada 1 da sala: digite 0\n')
            print('Lampada 2 da sala: digite 1\n')
            print('Arcondicionado: digite 2\n')
            print('Projetor multimídia: digite 3\n')
            escolheLed = int(input('Digite qual LED quer apagar: '))
            sala1.manipulaLed(0,escolheLed)

    elif(opcao == 3):
        print(f'\nEstado lampada 1: {sala1.getEstadoLampada1()}\n')
        print(f'Estado lampada 2: {sala1.getEstadoLampada2()}\n')
        print(f'Estado projetor: {sala1.getEstadoProjetor()}\n')
        print(f'Estado ar condicionado: {sala1.getEstadoArCondicionado()}\n')
        print(f'Estado sensor fumaça: {sala1.getEstadoSensorFumaca()}\n')
        print(f'Estado sensor presença: {sala1.getEstadoSensorPresenca()}\n')
        print(f'Estado sensor porta: {sala1.getEstadoSensorPorta()}\n')
        print(f'Estado sensor janela: {sala1.getEstadoSensorJanela()}\n')
        print(f'Estado alarme sala: {sala1.getEstadoAlarmeSala()}')
        

        # ENVIA PRO SERVIDOR
        # client1.enviaDados(f'Estado lampada 1: {sala1.getEstadoLampada1()}\n',conexao)
        # client1.enviaDados(f'Estado lampada 2: {sala1.getEstadoLampada2()}\n',conexao)
        # client1.enviaDados(f'Estado projetor: {sala1.getEstadoProjetor()}\n',conexao)
        # client1.enviaDados(f'Estado ar condicionado: {sala1.getEstadoArCondicionado()}\n',conexao)
        # client1.enviaDados(f'Estado sensor fumaça: {sala1.getEstadoSensorFumaca()}\n',conexao)
        # client1.enviaDados(f'Estado sensor presença: {sala1.getEstadoSensorPresenca()}\n',conexao)
        # client1.enviaDados(f'Estado sensor porta: {sala1.getEstadoSensorPorta()}\n',conexao)
        # client1.enviaDados(f'Estado sensor janela: {sala1.getEstadoSensorJanela()}\n',conexao)
        # client1.enviaDados(f'Estado alarme da sala: {sala1.getEstadoAlarmeSala()}\n',conexao)
        
        
    elif(opcao == 4):
        if(sala1.getEstadoAlarmeSala() == 0):
            sala1.setEstadoAlarmeSala(1)
            print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())
        elif(sala1.getEstadoAlarmeSala() == 1):
            sala1.setEstadoAlarmeSala(0)
            print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())
    
    else: print('Opção inválida!')
    

def main():
    while(1):
        
        alarmeSala = threading.Thread(sala1.alarmeSala())
        alarmeSala.start()
        # sala1.alarmeSala()
        sala1.temperatura(dhtDevice) #only 2 secs
        # Menu = threading.Thread(target=menu())
        # Menu.run()
        menu()


if __name__ == '__main__':
    main()
