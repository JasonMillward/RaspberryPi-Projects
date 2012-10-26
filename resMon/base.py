#!/usr/bin/env python

# Take cpu load percentate, *100 / 6.25


from itertools import cycle
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


DATA_PIN = 17
CLOCK_PIN = 21
LATCH_PIN = 22


GPIO.setup(DATA_PIN, GPIO.OUT)
GPIO.setup(CLOCK_PIN, GPIO.OUT)
GPIO.setup(LATCH_PIN, GPIO.OUT)

def digital_write(pin, value):
    GPIO.output(latch_pin, True)
    path = '/sys/class/gpio/gpio%d/value' % pin
        with open(path, 'w') as f:
                f.write('1' if value else '0')

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

def main():
        init()
        filename = 'animation.txt'
        for frame in cycle(read_lines(filename)):
                #print frame
                for pixel in frame:
                        shift_bit(pixel == '#')
                latch()
                sleep(0.05)

if __name__ == '__main__':
        main()
