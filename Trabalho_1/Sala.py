import RPi.GPIO as GPIO
class Sala():
    def __init__(self) -> None:
        pass 
    def getTemperatura():
        pass
    def manipulaLed(self,num,pos):
        
        led = [18,24,23]

        if(num==1): 
            GPIO.output(led[pos], GPIO.HIGH)
        else:
            GPIO.output(led[pos], GPIO.LOW)
