#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

LED_PIN = 12
SWITCH_PIN = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN)

status = GPIO.LOW
GPIO.output(LED_PIN, status)

while True:
	if GPIO.input(SWITCH_PIN) == 1:
		if status == GPIO.LOW:
			status = GPIO.HIGH
		else:
			status = GPIO.LOW
		GPIO.output(LED_PIN, status)

GPIO.cleanup()


