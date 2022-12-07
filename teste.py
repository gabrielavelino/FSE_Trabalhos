from gpiozero import LED
from time import sleep

led = [2,3,4]

for i in range(4):
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
    