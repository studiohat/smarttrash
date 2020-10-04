import RPi.GPIO as GPIO
import time

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(12) 
        time.sleep(3)

        p.ChangeDutyCycle(1)
        time.sleep(5)

except KeybordInterrupt:

     p.stop()

GPIO.cleanup()
