import RPi.GPIO as gpio
import time
OUT_0=5
OUT_1=6
OUT_2=13

E1=20
E2=21
E3=19

#gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(OUT_0,gpio.OUT)
gpio.setup(OUT_1,gpio.OUT)
gpio.setup(OUT_2,gpio.OUT)

gpio.setup(E1,gpio.OUT)
gpio.setup(E2,gpio.OUT)
gpio.setup(E3,gpio.OUT)

H=True
L=False
#gpio.output(E3,H)
#gpio.output(E2,L)
#gpio.output(E1,L)
#   0       1       2       3       4       5       6       7
RV=[[L,L,L],[H,L,L],[L,H,L],[H,H,L],[L,L,H],[H,L,H],[L,H,H],[H,H,H]]

def outputNum(num):
    gpio.output(OUT_0,RV[num][0])
    gpio.output(OUT_1,RV[num][1])
    gpio.output(OUT_2,RV[num][2])
    #print num, RV[num]
i=0
if H:
    t=0.5
    outputNum(2)
    time.sleep(t)
    #outputNum(1)
    #time.sleep(t)
    #outputNum(2)
    #time.sleep(t)
    #outputNum(3)
    
else:
    for i in range(12):
        print i%8,
        outputNum(i%8)
        time.sleep(0.5)

#time.sleep(2)
gpio.cleanup()
    
