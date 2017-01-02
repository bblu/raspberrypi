import RPi.GPIO as GPIO  
import time  
pins = [17,18]  
def setup():  
    GPIO.setmode(GPIO.BCM)  
    for pin in pins:  
        GPIO.setup(pin, GPIO.OUT)  
        GPIO.output(pin, GPIO.LOW) 

def loop():  
    tm=0.5
    while tm > 0.009:  
        for pin in pins:  
            GPIO.output(pin, GPIO.HIGH)  
            time.sleep(tm)  
            GPIO.output(pin, GPIO.LOW)  
            time.sleep(tm)
            if tm > 0.05:
                tm = tm-0.01
def destroy():  
    for pin in pins:  
        GPIO.output(pin, GPIO.LOW)  
        GPIO.setup(pin, GPIO.IN)  
if __name__ == '__main__':  
    setup()  
    try:  
        loop()  
    except KeyboardInterrupt:  
        destroy()  
