#!/usr/bin/env python
#
# Python Script for controlling VBS lighting modules from a Raspberry Pi
#
# Written By Les Holdeman 02/2018 using Python documentation:
# smbus - https://pypi.python.org/pypi/smbus2/0.2.0
# socket - https://docs.python.org/2/library/socket.html
# time - https://docs.python.org/2/library/time.html modules
#
# Commands for various colors of each LED 
# LED 1 Red			-	<addr> 0x14 0x01
# LED 1 Green		-	<addr> 0x14 0x02
# LED 1 Yellow		-	<addr> 0x14 0x03
# LED 1 Blue		-	<addr> 0x14 0x04
# LED 1 Purple		-	<addr> 0x14 0x05
# LED 1 Light Blue	-	<addr> 0x14 0x06
# LED 1 White		-	<addr> 0x14 0x07
#
# LED 2 Red			-	<addr> 0x14 0x08
# LED 2 Green 		-	<addr> 0x14 0x10
# LED 2 Yellow		-	<addr> 0x14 0x18
# LED 2 Blue		-	<addr> 0x14 0x20
# LED 2 Purple		-	<addr> 0x14 0x28
# LED 2 Light Blue	-	<addr> 0x14 0x30
# LED 2 White		-	<addr> 0x14 0x38
#
# LED 3 Red			-	<addr> 0x14 0x40
# LED 3 Green		-	<addr> 0x14 0x80
# LED 3 Yellow		-	<addr> 0x14 0xC0
# LED 3 Blue		-	<addr> 0x15 0x01
# LED 3 Purple		-	<addr> 0x14 0x40 and <addr> 0x15 0x01
# LED 3 Light Blue	-	<addr> 0x14 0x80 and <addr> 0x15 0x01
# LED 3 White		-	<addr> 0x14 0xC0 and <addr> 0x15 0x01
#
# LED 4 Red			-	<addr> 0x15 0x02
# LED 4 Green		-	<addr> 0x15 0x04
# LED 4 Yellow		-	<addr> 0x15 0x06
# LED 4 Blue		-	<addr> 0x15 0x08
# LED 4 Purple		-	<addr> 0x15 0x0A
# LED 4 Light Blue	-	<addr> 0x15 0x0C
# LED 4 White		-	<addr> 0x15 0x0E
#
# LED 5 Red			-	<addr> 0x15 0x10
# LED 5 Green		-	<addr> 0x15 0x20
# LED 5 Yellow		-	<addr> 0x15 0x30
# LED 5 Blue		-	<addr> 0x15 0x40
# LED 5 Purple		-	<addr> 0x15 0x50
# LED 5 Light Blue	-	<addr> 0x15 0x60
# LED 5 White		-	<addr> 0x15 0x70
#
# Standby LEDs		-	<addr> 0x15 0x80


import smbus
import time
import socket

#variables
bus = smbus.SMBus(1) # Use 1 for Rev 2 Pi, Use 0 for Rev 1 Pi
swirlTime = 0.1
blinkTime = 0.2

# Device Addresses
device0 = 0x20
device1 = 0x21


# Registers A are for GPA pins, Registers B are for GPB pins
IODIRA = 0x00 # Register A for pin direction
IODIRB = 0x01 # Register B for pin direction
OLATA = 0x14 # Register A for outputs
OLATB = 0x15 # Register B for outputs

# Setup
# Set GPA and GPB pins to outputs on all devices
bus.write_byte_data(device0,IODIRA,0x00)
bus.write_byte_data(device0,IODIRB,0x00)
#bus.write_byte_data(device1,IODIRA,0x00)
#bus.write_byte_data(device1,IODIRB,0x00)
	
# Set all outputs to off on all devices
bus.write_byte_data(device0,OLATA,0x00)
bus.write_byte_data(device0,OLATB,0x00)
#bus.write_byte_data(device1,OLATA,0x00)
#bus.write_byte_data(device1,OLATB,0x00)

# Functions
def idleState(addr):
	bus.write_byte_data(addr,OLATB,0x80)
	return;

def redSwirl(addr):
	bus.write_byte_data(addr,OLATA,0x01)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x08)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x40)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x02)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x10)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(swirlTime)
	return;
	
def blueSwirl(addr):
	bus.write_byte_data(addr,OLATA,0x02)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x10)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x80)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x04)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x20)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(swirlTime)
	return;
	
def greenSwirl(addr):
	bus.write_byte_data(addr,OLATA,0x04)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x20)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x01)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x08)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x40)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(swirlTime)
	return;

def purpleSwirl(addr):
	bus.write_byte_data(addr,OLATA,0x03)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x18)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0xc0)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x06)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x30)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(swirlTime)
	return;	
	
def yellowSwirl(addr):
	bus.write_byte_data(addr,OLATA,0x05)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x28)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x40)
	bus.write_byte_data(addr,OLATB,0x01)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x0A)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x50)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(swirlTime)
	return;
	
def lightBlueSwirl(addr):
	bus.write_byte_data(addr,OLATA,0x06)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x30)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x80)
	bus.write_byte_data(addr,OLATB,0x01)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x0C)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x60)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(swirlTime)
	return;

def whiteSwirl(addr):
	bus.write_byte_data(addr,OLATA,0x07)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x38)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0xC0)
	bus.write_byte_data(addr,OLATB,0x01)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x0E)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x70)
	time.sleep(swirlTime)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(swirlTime)
	return;
	
def redBlink(addr):
	bus.write_byte_data(addr,OLATA,0x49)
	bus.write_byte_data(addr,OLATB,0x12)
	time.sleep(blinkTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(blinkTime)
	return;
	
def blueBlink(addr):
	bus.write_byte_data(addr,OLATA,0x92)
	bus.write_byte_data(addr,OLATB,0x24)
	time.sleep(blinkTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(blinkTime)
	return;

def purpleBlink(addr):
	bus.write_byte_data(addr,OLATA,0xDB)
	bus.write_byte_data(addr,OLATB,0x36)
	time.sleep(blinkTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(blinkTime)
	return;
	
def greenBlink(addr):
	bus.write_byte_data(addr,OLATA,0x24)
	bus.write_byte_data(addr,OLATB,0x49)
	time.sleep(blinkTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(blinkTime)
	return;

def yellowBlink(addr):
	bus.write_byte_data(addr,OLATA,0x6D)
	bus.write_byte_data(addr,OLATB,0x5B)
	time.sleep(blinkTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(blinkTime)
	return;
	
def lightBlueBlink(addr):
	bus.write_byte_data(addr,OLATA,0xB6)
	bus.write_byte_data(addr,OLATB,0x6D)
	time.sleep(blinkTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(blinkTime)
	return;
	
def whiteBlink(addr):
	bus.write_byte_data(addr,OLATA,0xFF)
	bus.write_byte_data(addr,OLATB,0x7F)
	time.sleep(blinkTime)
	bus.write_byte_data(addr,OLATA,0x00)
	bus.write_byte_data(addr,OLATB,0x00)
	time.sleep(blinkTime)
	return;
	
	
def goodState():
	
	return;
	
def badState():

	return;
	
def errorState():
	purpleBlink(device0)
	purpleBlink(device1)
	return;


# Start the loop
while True :
    lightBlueBlink(device0)
    lightBlueSwirl(device0)
    blueBlink(device0)
    blueSwirl(device0)
    purpleBlink(device0)
    purpleSwirl(device0)
    redBlink(device0)
    redSwirl(device0)
    yellowBlink(device0)
    yellowSwirl(device0)
    greenBlink(device0)
    greenSwirl(device0)
    whiteBlink(device0)
    whiteSwirl(device0)

