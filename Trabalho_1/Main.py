from Sala import Sala
from time import sleep
import RPi.GPIO as GPIO

sala_1 = Sala()

GPIO.setmode(GPIO.BCM)
GPIO.setup([18,24,23],GPIO.OUT)

sala_1.manipulaLed(1,2)
sleep(1)
sala_1.manipulaLed(0,2)
sleep(1)
sala_1.manipulaLed(1,2)
sleep(1)
sala_1.manipulaLed(0,2)