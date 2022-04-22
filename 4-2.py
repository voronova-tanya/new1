import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decima2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
p = float(input())
try:
    a = 0
    while True:
        number = decima2binary(a%256)
        for i in range(len(dac)):
            GPIO.output(dac[i], number[i])
        time.sleep(p/512)
        a += 1
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

