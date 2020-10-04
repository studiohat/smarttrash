import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from time import sleep
import os

hand_detect = 22
can_mortor = 21
trash_detect = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(hand_detect, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(can_mortor, GPIO.OUT)

motor = GPIO.PWM(can_mortor, 50) #PMW : 펄스 폭 변조
motor.start(0)
count = 0

while True:
	if GPIO.input(hand_detect):
		
		#Server
#		os.system('bash /home/pi/photo.sh')
		
		#Motor
		#var = 값 받아오기
		if(var == can_mortor):
			motor.ChangeDutyCycle(12) #값은 바꿔야함
			time.sleep(10)
			motor.ChangeDutyCycle(1)
		'''
		else if(~~~):
			motor.ChangeDutyCycle(12.5)
			time.sleep(10)
		'''
		
		#Full Trash
		if not GPIO.input(trash_detect):
			count+=1
			sleep(1)
			if(count%5==0):
				#Alarm
			else:
				count=0
		
		break
		
try: 
    while True:
        time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()

