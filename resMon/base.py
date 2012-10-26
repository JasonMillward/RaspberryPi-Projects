#!/usr/bin/env python

# Currently rewriting code to use GPIO instead of /sys/classes/gpio pin outs
# Using Adafruits WebIDE on the Raspberry Pi
# 4th time using Python

# TODO: 
#   Get CPU Load
#   Take cpu load percentate, *100 / 6.25
#   Get Available RAM
#   Perform same maths
#   Output to radial LEDs
#   Check to see if sleep causes spikes in CPU - Update: It does not 


from itertools import cycle
from time import sleep
import RPi.GPIO as GPIO
import psutil


GPIO.setmode(GPIO.BCM)

DATA_PIN = 17
CLOCK_PIN = 21
LATCH_PIN = 22

GPIO.setup(DATA_PIN, GPIO.OUT)
GPIO.setup(CLOCK_PIN, GPIO.OUT)
GPIO.setup(LATCH_PIN, GPIO.OUT)

def digital_write(pin, value):
    GPIO.output(pin, '1' if value else '0')


def init():
    digital_write(data_pin, 0)
    digital_write(clock_pin, 0)
    digital_write(latch_pin, 0)

def shift_bit(value):
    digital_write(data_pin, value)
    digital_write(clock_pin, 1)
    digital_write(clock_pin, 0)

def latch():
    digital_write(latch_pin, 1)
    digital_write(latch_pin, 0)

def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
            
def dec_to_bit(x):
    output = ""
    for y in range(1, 16):
        if x > 1:
            x = x - 1
            output = "1" + output
        else:
            output = "0" + output 
    
    return output
    
    
def main():
    #init()  
    while True:
        memory = psutil.phymem_usage()
        memoryLED =  int(memory[3] / 6.25)    
        cpuLED =  int(psutil.cpu_percent(interval=1) / 6.25)
         
        print "Memory LEDs to light up: %d" % memoryLED
        print "CPU LEDs to light up:    %d" % cpuLED
        
        bits = dec_to_bit(memoryLED)
        
        for c in bits:
            print c
        sleep(5)

    #for frame in cycle(read_lines(filename)):
    #        #print frame
    #        for pixel in frame:
    #                shift_bit(pixel == '#')
    #        latch()
    #        sleep(0.05)

if __name__ == '__main__':
    main()
