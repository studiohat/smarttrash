import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
BUZ = 27
ON = 1
OFF = 0
GPIO.setup(BUZ, GPIO.OUT)
ck_pwm = GPIO.PWM(BUZ, 1000)
ck_pwm.start(50)
time.sleep(1000)
ck_pwm.stop()
