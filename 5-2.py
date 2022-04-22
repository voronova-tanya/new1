import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
comp = 4
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decima2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    l = 0
    r = 255
    for i in range(8):
        ans = l + (r - l)//2
        signal = num2dac(ans)
        time.sleep(0.01)
        voltage = i / (2**8) * 3.3
        GPIO.output(dac, decima2binary(i))
        if GPIO.input(comp) == 0:
            r = ans
        else:
            l = ans
    return 3.3*(l + (r - l)//2)/256
    
def num2dac(value):
    signal = decima2binary(value)
    GPIO.output(dac, signal)
    return signal
try:
    while True:
        print(adc())
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

