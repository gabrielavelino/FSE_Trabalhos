from Sala import Sala
from time import sleep
import RPi.GPIO as GPIO
# import GPIOZERO as LED

sala_1 = Sala()

GPIO.setmode(GPIO.BCM)
GPIO.setup([18,23,24,25],GPIO.OUT)


def menu():
    print('1 - Ligar lampada')
    print('2 - Desligar lampada')
    print('3 - Estados em tempo real')
    print('4 - Verificar lista de comandos')
    print('5 - Sair do programa')

# def sairLoop(sair):
#     sair = str(input('Deseja sair? [y,n]: '))
#     if (sair == 'y'):
#         break
#     else:
#         continue

def main():
    while(1):
        menu()
        opcao = int(input('Digite sua opcao: '))
        
        if(opcao == 1):
            # sala_1.manipulaLed(1,2)
            # sala_1.manipulaLed(1,1)
            # sleep(1)
            # sala_1.manipulaLed(0,2)
            # sala_1.manipulaLed(0,1)
            # sleep(1)
            # sala_1.manipulaLed(1,2)
            # sala_1.manipulaLed(1,1)
            # sleep(1)
            # sala_1.manipulaLed(0,1)
            # sala_1.manipulaLed(0,2)
            while True:
                escolheLed = int(input('Digite qual LED quer acender: '))
                sala_1.manipulaLed(1,escolheLed)
                sair = str(input('Deseja sair? [y,n]: '))
                if (sair == 'y'):
                    break
                else:
                    continue
        elif(opcao == 2):
            while True:
                escolheLed = int(input('Digite qual LED quer apagar: '))
                sala_1.manipulaLed(0,escolheLed)
                sair = str(input('Deseja sair? [y,n]: '))
                if (sair == 'y'):
                    break
                else:
                    continue

            
        
        elif(opcao == 3):
            print('Ainda não implementado')
            break
        
        elif(opcao == 4):
            print('\n\n----------- Lista de comandos -------------\n')
            print('Lampada 1 da sala: digite 0\n')
            print('Lampada 2 da sala: digite 1\n')
            print('Arcondicionado: digite 2\n')
            print('Projetor multimídia: digite 3\n')
        elif(opcao == 5):
            break


if __name__ == '__main__':
    main()
