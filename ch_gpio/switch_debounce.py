#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

LED_PIN = 12
SWITCH_PIN = 11
TIME_LAPSE = 0.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN)

status = GPIO.LOW
GPIO.output(LED_PIN, status)
timemark = time.time()

while True:
	timemark2 = time.time()
	if GPIO.input(SWITCH_PIN) == GPIO.HIGH and (timemark2 - timemark) > TIME_LAPSE:
		timemark = timemark2
		if status == GPIO.LOW:
			status = GPIO.HIGH
		else:
			status = GPIO.LOW
		GPIO.output(LED_PIN, status)

GPIO.cleanup()


