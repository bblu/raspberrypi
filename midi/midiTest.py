# I Fule Python

import midi
import time
import ledDriver

pattern = midi.read_midifile('mary.mid')
print type(pattern)
#print ledDriver.__name__
print 'format:',pattern.format
print 'resolution:',pattern.resolution

track = pattern[1]

t=0.001
while True:
    time.sleep(t)
    ledDriver.showDigit(1,4,False)
    time.sleep(t)
    ledDriver.showDigit(2,3,False)
    time.sleep(t)
    ledDriver.showDigit(3,2,False)
    time.sleep(t)
    ledDriver.showDigit(4,1,False)
    

#ledDriver.clear()


