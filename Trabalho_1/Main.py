from Sala import Sala
from time import sleep
import RPi.GPIO as GPIO
# from variaveis import sala1
# import GPIOZERO as LED

sala1 = Sala(7, 1, 12, 16, 20, 21, 26)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup([18,23,24,25,8],GPIO.OUT)
GPIO.setup(sala1.sensor_fumaca,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(sala1.sensor_fumaca, GPIO.BOTH, callback=sala1.sensorFumaca,bouncetime = 300)

# def callErrado():
#     sala1.sensorFumaca()


def menu():
    print('1 - Ligar lampada')
    print('2 - Desligar lampada')
    print('3 - Estados em tempo real')
    print('4 - Verificar lista de comandos')
    print('5 - Sair do programa')


def main():
    while(1):
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
            print('Ainda não implementado')
            sala1.manipulaSensores()
            
        
        elif(opcao == 4):
            print('\n\n----------- Lista de comandos -------------\n')
            print('Lampada 1 da sala: digite 0\n')
            print('Lampada 2 da sala: digite 1\n')
            print('Arcondicionado: digite 2\n')
            print('Projetor multimídia: digite 3\n')
            print('Alarme: digite 4\n')
        elif(opcao == 5):
            break


if __name__ == '__main__':
    main()
