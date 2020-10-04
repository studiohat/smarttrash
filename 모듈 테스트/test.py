import RPi.GPIO as GPIO
import time

pin =21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)  #PMW:펄스 폭 변조
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(7.5) 
        time.sleep(1)
        
        p.ChangeDutyCycle(2.5)
        time.sleep(5)


except KeybordInterrupt:

     p.stop()

GPIO.cleanup()
