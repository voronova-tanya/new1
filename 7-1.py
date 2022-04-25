import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
troyka = 17
comp=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(troyka, GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

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
measured_data=[]
try:
    while True:
        GPIO.output(troyka, GPIO.HIGH)
        t_1=time.time()
        s=adc()
        measured_data=[].append(s)
        a = int(s/3.3*9)
        led = [0] * (8-a) + [1] * a
        for i, j in enumerate(leds):
            GPIO.output(j, led[i])
        if s>3.201:# полная зарядка
              GPIO.output(troyka,0)
              while s>0.066:
                 
                 measured_data=[].append(s)
                 a = int(s/3.3*9)
                 led = [0] * (8-a) + [1] * a
                 for i, j in enumerate(leds):
                     GPIO.output(j, led[i])
                 print(s)
              t_2=time.time()
              continue
        print(s)
    t=t_2-t_1 # Время измерений
    plt.plot(measured_data)
    plt.show()
    measured_data_str=[str(item) for item in measured_data]

    with open('data.txt','w') as outfile:
        outfile.write('\n'.join(measured_data_str))
    with open('settings.txt','w') as outfile:
        chastota=(len(measured_data))/t
        step=str(3.201/255)
        outfile.write('\n'.join(chastota, step))   
    print(t, t/(len(measured_data)), chastota,step)    
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()

'''
measured_data=[]
plt.plot(measured_data)
plt.show()
measured_data_str=[str(item) for item in measured_data]
with open('data.txt','w') as outfile:
    outfile.write('\n'.join(measured_data_str))'''