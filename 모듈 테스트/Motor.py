import RPi.GPIO as GPIO
import time

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)  #PMW:펄스 폭 변조
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(12) #최댓값
        time.sleep(5)

        p.ChangeDutyCycle(1) #0
        time.sleep(3)

except KeybordInterrupt:

     p.stop()

GPIO.cleanup()
