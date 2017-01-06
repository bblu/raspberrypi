import RPi.GPIO as gpio
import time
OUT_0=5
OUT_1=6
OUT_2=13

E1=20
E2=21
E3=19

H=True
L=False
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(OUT_0,gpio.OUT)
gpio.setup(OUT_1,gpio.OUT)
gpio.setup(OUT_2,gpio.OUT)

gpio.setup(E1,gpio.OUT)
gpio.setup(E2,gpio.OUT)
gpio.setup(E3,gpio.OUT)

#gpio.output(OUT_0,L)
#gpio.output(OUT_1,H)
#gpio.output(OUT_2,H)

def outputNum(num):
    if num==0:
        gpio.output(OUT_0,L)
        gpio.output(OUT_1,L)
        gpio.output(OUT_2,L)
    elif num==1:
        gpio.output(OUT_0,H)
        gpio.output(OUT_1,L)
        gpio.output(OUT_2,L)
    elif num==2:
        gpio.output(OUT_0,L)
        gpio.output(OUT_1,H)
        gpio.output(OUT_2,L)
    elif num==3:
        gpio.output(OUT_0,H)
        gpio.output(OUT_1,H)
        gpio.output(OUT_2,L)
    elif num==4:
        gpio.output(OUT_0,L)
        gpio.output(OUT_1,L)
        gpio.output(OUT_2,H)
    elif num==5:
        gpio.output(OUT_0,H)
        gpio.output(OUT_1,L)
        gpio.output(OUT_2,H)
    elif num==6:
        gpio.output(OUT_0,L)
        gpio.output(OUT_1,H)
        gpio.output(OUT_2,H)
    elif num==7:
        gpio.output(OUT_0,H)
        gpio.output(OUT_1,H)
        gpio.output(OUT_2,H)


for i in range(864):
    outputNum(i%8)
    time.sleep(0.05)
    
