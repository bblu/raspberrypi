# I Fule Python

import midi
import ledDriver
pattern = midi.read_midifile('mary.mid')
print type(pattern)
#print ledDriver.__name__
print pattern.format
print pattern.resolution
print pattern.count('track')
track = pattern[1]

for event in track:
    print event.tick


ledDriver.clear()


