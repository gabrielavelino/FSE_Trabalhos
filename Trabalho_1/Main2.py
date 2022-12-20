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

sala2 = Sala(0, 11, 9, 10, 22, 27, 18)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup([26,19,13,6,5],GPIO.OUT)
dhtDevice = adafruit_dht.DHT22(board.D4)
GPIO.setup([sala2.sensor_fumaca,sala2.sensor_janela,sala2.sensor_porta,sala2.sensor_presenca,sala2.sensorContagemPessoasEntrada,sala2.sensorContagemPessoasSaida],GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(sala2.sensor_fumaca, GPIO.BOTH, callback=sala2.sensorFumaca,bouncetime = 300)
GPIO.add_event_detect(sala2.sensor_janela, GPIO.BOTH, callback=sala2.sensorJanela,bouncetime = 300)
GPIO.add_event_detect(sala2.sensor_porta, GPIO.BOTH, callback=sala2.sensorPorta,bouncetime = 300)
GPIO.add_event_detect(sala2.sensor_presenca, GPIO.BOTH, callback=sala2.sensorPresenca,bouncetime = 300)
GPIO.add_event_detect(sala2.sensorContagemPessoasEntrada, GPIO.RISING, callback=sala2.sensorEntradaPessoas,bouncetime = 300)
GPIO.add_event_detect(sala2.sensorContagemPessoasSaida, GPIO.RISING, callback=sala2.sensorSaidaPessoas,bouncetime = 300)



def menu():
    print('Número de pessoa na sala: ', sala2.getEstadoSensorPessoasEntrada())
    print('\n######### Sala automatiza ##########\n')
    print('1 - Ligar lampadas - projetor - ar condicionado')
    print('2 - Desligar lampada')
    print('3 - Estados em tempo real')
    print('4 - Ligar alarme (somente quando não tem ninguém na sala!)')
    client1.recebeDados(conexao,FORMAT,sala2,GPIO)
    opcao = int(input('Digite sua opcao: '))

    if(opcao == 1):
        print('\n\n----------- Lista de comandos -------------\n')
        print('Lampada 1 da sala: digite 0\n')
        print('Lampada 2 da sala: digite 1\n')
        print('Arcondicionado: digite 2\n')
        print('Projetor multimídia: digite 3\n')
        print('Alarme: digite 4\n')
        escolheLed = int(input('Digite qual LED quer acender: '))
        sala2.manipulaLedSala2(1,escolheLed)
        
    elif(opcao == 2):
            print('\n\n----------- Lista de comandos -------------\n')
            print('Lampada 1 da sala: digite 0\n')
            print('Lampada 2 da sala: digite 1\n')
            print('Arcondicionado: digite 2\n')
            print('Projetor multimídia: digite 3\n')
            escolheLed = int(input('Digite qual LED quer apagar: '))
            sala2.manipulaLedSala2(0,escolheLed)

    elif(opcao == 3):
        print(f'\nEstado lampada 1: {sala2.getEstadoLampada1()}\n')
        print(f'Estado lampada 2: {sala2.getEstadoLampada2()}\n')
        print(f'Estado projetor: {sala2.getEstadoProjetor()}\n')
        print(f'Estado ar condicionado: {sala2.getEstadoArCondicionado()}\n')
        print(f'Estado sensor fumaça: {sala2.getEstadoSensorFumaca()}\n')
        print(f'Estado sensor presença: {sala2.getEstadoSensorPresenca()}\n')
        print(f'Estado sensor porta: {sala2.getEstadoSensorPorta()}\n')
        print(f'Estado sensor janela: {sala2.getEstadoSensorJanela()}\n')
        print(f'Estado alarme sala: {sala2.getEstadoAlarmeSala()}')
        

        # ENVIA PRO SERVIDOR
        # client1.enviaDados(f'Estado lampada 1: {sala2.getEstadoLampada1()}\n',conexao)
        # client1.enviaDados(f'Estado lampada 2: {sala2.getEstadoLampada2()}\n',conexao)
        # client1.enviaDados(f'Estado projetor: {sala2.getEstadoProjetor()}\n',conexao)
        # client1.enviaDados(f'Estado ar condicionado: {sala2.getEstadoArCondicionado()}\n',conexao)
        # client1.enviaDados(f'Estado sensor fumaça: {sala2.getEstadoSensorFumaca()}\n',conexao)
        # client1.enviaDados(f'Estado sensor presença: {sala2.getEstadoSensorPresenca()}\n',conexao)
        # client1.enviaDados(f'Estado sensor porta: {sala2.getEstadoSensorPorta()}\n',conexao)
        # client1.enviaDados(f'Estado sensor janela: {sala2.getEstadoSensorJanela()}\n',conexao)
        # client1.enviaDados(f'Estado alarme da sala: {sala2.getEstadoAlarmeSala()}\n',conexao)
        
        
    elif(opcao == 4):
        if(sala2.getEstadoAlarmeSala() == 0):
            sala2.setEstadoAlarmeSala(1)
            print('Estado alarme sala: ',sala2.getEstadoAlarmeSala())
        elif(sala2.getEstadoAlarmeSala() == 1):
            sala2.setEstadoAlarmeSala(0)
            print('Estado alarme sala: ',sala2.getEstadoAlarmeSala())
    
    else: print('Opção inválida!')
    

def main():
    while(1):
        
        alarmeSala = threading.Thread(sala2.alarmeSala())
        alarmeSala.start()
        # sala2.alarmeSala()
        # sala2.temperatura(dhtDevice) #only 2 secs
        # Menu = threading.Thread(target=menu())
        # Menu.run()
        menu()


if __name__ == '__main__':
    main()
