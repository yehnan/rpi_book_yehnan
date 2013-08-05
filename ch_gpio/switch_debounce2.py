#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

LED_PIN = 13
SWITCH_PIN = 11
BOUNCETIME = 200

GPIO.setmode(GPIO.BOARD)
status = GPIO.LOW
GPIO.setup(LED_PIN, GPIO.OUT, initial=status)
GPIO.setup(SWITCH_PIN, GPIO.IN)

def switchCallback(channel):
	global status
	if status == GPIO.LOW:
		status = GPIO.HIGH
	else:
		status = GPIO.LOW
	GPIO.output(LED_PIN, status)

GPIO.add_event_detect(SWITCH_PIN, GPIO.RISING, callback=switchCallback, bouncetime=BOUNCETIME)

while True:
	time.sleep(1)

GPIO.cleanup()


