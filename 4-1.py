import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decima2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        a = input()
        if str(a) == 'q':
            break
        elif not a.isnumeric():
            print('Введено не числовое значение')
        else:
            a = int(a)
            if a < 0 or a > 255:
                print('Неверный ввод')
            else:
                number = decima2binary(a)
                for i in range(len(dac)):
                    GPIO.output(dac[i], number[i])
                U = float(3.3)
                D = int(256)
                u = U*a/D
                print(float(u))
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


