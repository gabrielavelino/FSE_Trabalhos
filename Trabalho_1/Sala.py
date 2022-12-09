import RPi.GPIO as GPIO

class Sala():

    # def __init__(self,lampada_1,lampada_2):
        
    #     self.lampada_1 = lampada_1
    #     self.lampada_2 = lampada_2
   
   
    def getTemperatura():
        pass
    
    def pegaEstado(self,estado):
        pass
    
    def manipulaLed(self,num,pos):
        
        led = [18,23,24,25]

        if(num==1): 
            GPIO.output(led[pos], GPIO.HIGH)
        else:
            GPIO.output(led[pos], GPIO.LOW)
