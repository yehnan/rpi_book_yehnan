#!/usr/bin/env python

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)

def readadc(ch):
    if ch > 7 or ch < 0:
        return -1
    rst = spi.xfer2([1, (8 + ch) << 4, 0])
    adcout = ((rst[1] & 0x03) << 8) + rst[2]
    return adcout

while True:
    for i in range(0, 2):
        print("Ch " + str(i) + " = " + str(readadc(i)))
    time.sleep(1)


