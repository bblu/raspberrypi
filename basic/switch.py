import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.IN)
gpio.setup(18,gpio.OUT)
gpio.output(18, gpio.LOW)

pwm=gpio.PWM(18, 10)
pwm.start(0)

def breath():
    # dark to light
    for i in xrange(0, 101, 1):
        pwm.ChangeDutyCycle(i)
        time.sleep(.02)

    # light to dark
    for i in xrange(100, -1, -1):
        pwm.ChangeDutyCycle(i)
        time.sleep(.02)

try:
 while True:
    if(gpio.input(17)==True):
        #gpio.output(18, gpio.HIGH)
        breath()
    #else:
        #gpio.output(18, gpio.LOW)
except KeyboardInterrupt:
    pass

pwm.stop()
gpio.cleanup()

