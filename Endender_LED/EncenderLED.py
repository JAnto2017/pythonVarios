import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
speed=2
while True:
	GPIO.output(7,True)
	time.sleep(speed)
	GPIO.output(7,False)
	time.sleep(speed)
	
	
