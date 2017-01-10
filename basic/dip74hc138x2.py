import RPi.GPIO as gpio
import time
OUT_0=2
OUT_1=3
OUT_2=4
OUT_3=5


#gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(OUT_0,gpio.OUT)
gpio.setup(OUT_1,gpio.OUT)
gpio.setup(OUT_2,gpio.OUT)
gpio.setup(OUT_3,gpio.OUT)


H=True
L=False
#gpio.output(E3,H)
#gpio.output(E2,L)
#gpio.output(E1,L)
#   0       1       2       3       4       5       6       7
RV=[[L,L,L,L],[H,L,L,L],[L,H,L,L],[H,H,L,L],[L,L,H,L],[H,L,H,L],[L,H,H,L],[H,H,H,L],
    [L,L,L,H],[H,L,L,H],[L,H,L,H],[H,H,L,H],[L,L,H,H],[H,L,H,H],[L,H,H,H],[H,H,H,H]]

def outputNum(num):
    gpio.output(OUT_0,RV[num][0])
    gpio.output(OUT_1,RV[num][1])
    gpio.output(OUT_2,RV[num][2])
    gpio.output(OUT_3,RV[num][3])
    #print num, RV[num]
while True:
    
    for i in range(16):
        outputNum(i)
        if i%2==0:
            time.sleep(0.25)
        else:
            time.sleep(0.1)
            

    
