#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

LED_PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0)

while True:
	for dc in range(0, 101, 5):
		pwm.ChangeDutyCycle(dc)
		time.sleep(0.1)
	for dc in range(100, -1, -5):
		pwm.ChangeDutyCycle(dc)
		time.sleep(0.1)

pwm.stop()
GPIO.cleanup()


