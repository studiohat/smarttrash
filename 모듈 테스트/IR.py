import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from time import sleep
import os

pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

while True:
	if GPIO.input(pin):
		
		#Camera
		camera = PiCamera()
		camera.start_preview()
		sleep(3)
		camera.capture('/home/pi/Photo/image.jpg')
		camera.stop_preview()
		
		#Motor
		
		
		#Server
		os.system('bash /home/pi/photo.sh')
		
		break
    
try: 
    while True:
        time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()
