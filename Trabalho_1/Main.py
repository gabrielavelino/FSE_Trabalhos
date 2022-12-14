from Sala import Sala
from time import sleep
import RPi.GPIO as GPIO
import board
import adafruit_dht

# from variaveis import sala1
# import GPIOZERO as LED

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

# def callErrado():
#     sala1.sensorFumaca()


def menu():
    print('1 - Ligar lampada')
    print('2 - Desligar lampada')
    print('3 - Estados em tempo real')
    print('4 - Verificar lista de comandos')
    print('5 - Ligar alarme (somente quando não tem ninguém na sala!)')
    print('6 - Sair do programa')
    


def main():
    while(1):
        sala1.alarmeSala()
        sala1.temperatura(dhtDevice) #only 2 secs
        menu()
        opcao = int(input('Digite sua opcao: '))
        
        if(opcao == 1):
            # sala1.manipulaLed(1,2)
            # sleep(1)
            # sala1.manipulaLed(0,2)
            
            while True:
                escolheLed = int(input('Digite qual LED quer acender: '))
                sala1.manipulaLed(1,escolheLed)
                sair = str(input('Deseja sair? [y,n]: '))
                if (sair == 'y'):
                    break
                else:
                    continue
        elif(opcao == 2):
            while True:
                escolheLed = int(input('Digite qual LED quer apagar: '))
                sala1.manipulaLed(0,escolheLed)
                sair = str(input('Deseja sair? [y,n]: '))
                if (sair == 'y'):
                    break
                else:
                    continue

            
        
        elif(opcao == 3):
            print('\nEstado sensor fumaça: ' + str(sala1.getEstadoSensorFumaca()) + '\n')
            print('\nEstado sensor presença: ' + str(sala1.getEstadoSensorPresenca()) + '\n')
            print('\nEstado sensor porta: ' + str(sala1.getEstadoSensorPorta()) + '\n')
            print('\nEstado sensor janela: ' + str(sala1.getEstadoSensorJanela()) + '\n')
            print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())
            
        
        elif(opcao == 4):
            print('\n\n----------- Lista de comandos -------------\n')
            print('Lampada 1 da sala: digite 0\n')
            print('Lampada 2 da sala: digite 1\n')
            print('Arcondicionado: digite 2\n')
            print('Projetor multimídia: digite 3\n')
            print('Alarme: digite 4\n')
        
        elif(opcao == 5):
            if(sala1.getEstadoAlarmeSala() == 0):
                sala1.setEstadoAlarmeSala(1)
                print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())
            elif(sala1.getEstadoAlarmeSala() == 1):
                sala1.setEstadoAlarmeSala(0)
                print('Estado alarme sala: ',sala1.getEstadoAlarmeSala())

        elif(opcao == 6):
            break


if __name__ == '__main__':
    main()
