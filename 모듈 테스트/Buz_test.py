import RPi.GPIO as GPIO
import time
from time import sleep
import os

trash_detect = 23
buzzer = 27


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trash_detect, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(buzzer, GPIO.OUT)

	
count = 0
	
def buzer() :
	ck_pwm = GPIO.PWM(buzzer, 1000)
	ck_pwm.start(50)
	time.sleep(10)
	

while True:
	if not GPIO.input(trash_detect):
		count+=1
		sleep(1)
		print(count)
		if(count%5==0):
		 buzer()	
		 continue
	else :
		count = 0
