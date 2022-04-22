import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
a = 21
GPIO.setup(2, GPIO.OUT)
def decima2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
p = GPIO.PWM(2, 1000)
p.start(0)
try:
    while True:
        n = input()
        if str(n) == 'q':
            break 
        else:
            n = int(n)
            p.start(n)
            n = input()
finally:
    p.stop()
    GPIO.output(2, 0)
    GPIO.cleanup()

