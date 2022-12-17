from Sala import Sala
from time import sleep
import RPi.GPIO as GPIO
import board
import adafruit_dht
import sys
from client import cliente

## SERVIDOR DISTRIBUIDO ###
HEADER = 128
PORT = 10471
HOST = sys.argv[-1]
# SERVER = sys.argv[-1]
# SERVER = "192.168.1.129"            ## 43
# SERVER = "192.168.1.146"            ## 44
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# ADDR = (SERVER, PORT)
ADDR = (HOST, PORT)

# from variaveis import sala1
# import GPIOZERO as LED

# INICIALIZA SALA
client1 = cliente(HEADER,PORT,HOST,ADDR)
conexao = client1.iniciaConexao() 
sala1 = Sala(7, 1, 12, 16, 20, 21, 26)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup([18,23,24,25,8],GPIO.OUT)
dhtDevice = adafruit_dht.DHT22(board.D4)
GPIO.setup([sala1.sensor_fumaca,sala1.sensor_janela,sala1.sensor_porta,sala1.sensor_presenca],GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(sala1.sensor_fumaca, GPIO.BOTH, callback=sala1.sensorFumaca,bouncetime = 300)
GPIO.add_event_detect(sala1.sensor_janela, GPIO.BOTH, callback=sala1.sensorJanela,bouncetime = 300)
GPIO.add_event_detect(sala1.sensor_porta, GPIO.BOTH, callback=sala1.sensorPorta,bouncetime = 300)
GPIO.add_event_detect(sala1.sensor_presenca, GPIO.BOTH, callback=sala1.sensorPresenca,bouncetime = 300)


def menu():
    
    print('\n######### Sala automatiza ##########\n')
    print('1 - Ligar lampadas - projetor - ar condicionado')
    print('2 - Desligar lampada')
    print('3 - Estados em tempo real')
    print('5 - Ligar alarme (somente quando não tem ninguém na sala!)')

    opcao = int(input('Digite sua opcao: '))

    if(opcao == 1):
            # sala1.manipulaLed(1,2)
            # sleep(1)
            # sala1.manipulaLed(0,2)
            
            while True:
                print('\n\n----------- Lista de comandos -------------\n')
                print('Lampada 1 da sala: digite 0\n')
                print('Lampada 2 da sala: digite 1\n')
                print('Arcondicionado: digite 2\n')
                print('Projetor multimídia: digite 3\n')
                print('Alarme: digite 4\n')
                escolheLed = int(input('Digite qual LED quer acender: '))
                sala1.manipulaLed(1,escolheLed)
                sair = str(input('Deseja sair? [y,n]: '))
                if (sair == 'y'):
                    break
                else:
                    continue
    elif(opcao == 2):
        while True:
            print('\n\n----------- Lista de comandos -------------\n')
            print('Lampada 1 da sala: digite 0\n')
            print('Lampada 2 da sala: digite 1\n')
            print('Arcondicionado: digite 2\n')
            print('Projetor multimídia: digite 3\n')
            escolheLed = int(input('Digite qual LED quer apagar: '))
            sala1.manipulaLed(0,escolheLed)
            sair = str(input('Deseja sair? [y,n]: '))
            if (sair == 'y'):
                break
            else:
                continue

    elif(opcao == 3):
        print(f'\nEstado lampada 1: {sala1.getEstadoLampada1()}\n')
        print(f'Estado lampada 2: {sala1.getEstadoLampada2()}\n')
        print(f'Estado projetor: {sala1.getEstadoProjetor()}\n')
        print(f'Estado ar condicionado: {sala1.getEstadoArCondicionado()}\n')
        print('Estado sensor fumaça: ' + str(sala1.getEstadoSensorFumaca()) + '\n')
        print('Estado sensor presença: ' + str(sala1.getEstadoSensorPresenca()) + '\n')
        print('Estado sensor porta: ' + str(sala1.getEstadoSensorPorta()) + '\n')
        print('Estado sensor janela: ' + str(sala1.getEstadoSensorJanela()) + '\n')
        print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())
        # ENVIA PRO SERVIDOR
        client1.send(f'Estado lampada 1: {sala1.getEstadoLampada1()}\n',conexao)
        client1.send(f'Estado lampada 2: {sala1.getEstadoLampada2()}\n',conexao)
        client1.send(f'Estado projetor: {sala1.getEstadoProjetor()}\n',conexao)
        client1.send(f'Estado ar condicionado: {sala1.getEstadoArCondicionado()}\n',conexao)
        client1.send(f'Estado sensor fumaça: {sala1.getEstadoSensorFumaca()}\n',conexao)
        client1.send(f'Estado sensor presença: {sala1.getEstadoSensorPresenca()}\n',conexao)
        client1.send(f'Estado sensor porta: {sala1.getEstadoSensorPorta()}\n',conexao)
        client1.send(f'Estado sensor janela: {sala1.getEstadoSensorJanela()}\n',conexao)
        client1.send(f'Estado alarme da sala: {sala1.getEstadoAlarmeSala()}\n',conexao)
        
        
    elif(opcao == 4):
        if(sala1.getEstadoAlarmeSala() == 0):
            sala1.setEstadoAlarmeSala(1)
            print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())
        elif(sala1.getEstadoAlarmeSala() == 1):
            sala1.setEstadoAlarmeSala(0)
            print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())


def main():
    while(1):
        sala1.alarmeSala()
        sala1.temperatura(dhtDevice) #only 2 secs
        menu()


if __name__ == '__main__':
    main()
