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


from time import sleep
import RPi.GPIO as GPIO
import psutil




DATA_PIN = 17
CLOCK_PIN = 21
LATCH_PIN = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(DATA_PIN, GPIO.OUT)
GPIO.setup(CLOCK_PIN, GPIO.OUT)
GPIO.setup(LATCH_PIN, GPIO.OUT)

def digital_write(pin, value):
    GPIO.output(pin, value)

def init():
    digital_write(DATA_PIN, 0)
    digital_write(CLOCK_PIN, 0)
    digital_write(LATCH_PIN, 0)

def shift_bit(value):
    digital_write(DATA_PIN, int(value))
    digital_write(CLOCK_PIN, 1)
    digital_write(CLOCK_PIN, 0)

def latch():
    digital_write(LATCH_PIN, 1)
    digital_write(LATCH_PIN, 0)

def shiftDec(x):
    bits = ""
    for y in range(1, 16):
        if x > 1:
            x = x - 1
            bits = "1" + bits
        else:
            bits = "0" + bits 

    print bits
    
    for bit in bits:
        shift_bit(bit)
    
    latch()

    
def main():
    init()
    a=0
    while True:
        a=a+1
        if a > 16:
            a=0
        #memory = psutil.phymem_usage()
        #memoryLED =  int(memory[3] / 6.25)    
        #cpuLED =  int(psutil.cpu_percent(interval=1) / 6.25)
         
        #print "Memory LEDs to light up: %d" % memoryLED
        #print "CPU LEDs to light up:    %d" % cpuLED
        shiftDec(0)
        shiftDec(11)
            
        sleep(1)


if __name__ == '__main__':
    main()
