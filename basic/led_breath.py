import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14, RPi.GPIO.OUT)

# GPIO=14#
pwm = RPi.GPIO.PWM(14, 70)
pwm.start(0)

try:
    while True:
        # dark to light
        for i in xrange(0, 101, 1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
            
        # light to dark
        for i in xrange(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)


except KeyboardInterrupt:
    pass

pwm.stop()
RPi.GPIO.cleanup()

