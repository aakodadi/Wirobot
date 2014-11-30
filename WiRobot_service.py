#!/usr/bin/python
# -*- coding: utf8 -*-

import RPIO as gpio
import sys

########## const_def_begin

# Select the GPIO channels
fcom = 21
bcom = 7

rcom = 26
lcom = 24

########## const_def_end

def end_WiRobot(): ########## end_WiRobot_begin
	gpio.cleanup()
	sys.exit()
	########## end_WiRobot_end

def init_WiRobot(): ########## init_WiRobot_begin
	# use P1 header pin numbering convention
	gpio.setmode(gpio.BOARD)

	# Set up the GPIO channels - one output
	gpio.setup(fcom, gpio.OUT, initial=gpio.LOW)
	gpio.setup(bcom, gpio.OUT, initial=gpio.LOW)
	gpio.setup(rcom, gpio.OUT, initial=gpio.LOW)
	gpio.setup(lcom, gpio.OUT, initial=gpio.LOW)

	# TCP socket server callback on port 2323
	gpio.add_tcp_callback(2323, socket_callback, threaded_callback=False)

	# Blocking main epoll loop
	gpio.wait_for_interrupts()
	########## init_WiRobot_end

def socket_callback(socket, val): ########## socket_callback_begin
	if 'S' in val:
		gpio.output(fcom, gpio.LOW)
		gpio.output(bcom, gpio.LOW)
		gpio.output(rcom, gpio.LOW)
		gpio.output(lcom, gpio.LOW)
		return
	if 'F' in val:
		gpio.output(fcom, gpio.HIGH)
		gpio.output(bcom, gpio.LOW)
		gpio.output(rcom, gpio.LOW)
		gpio.output(lcom, gpio.LOW)
		return
	if 'B' in val:
		gpio.output(fcom, gpio.LOW)
		gpio.output(bcom, gpio.HIGH)
		gpio.output(rcom, gpio.LOW)
		gpio.output(lcom, gpio.LOW)
		return
	if 'R' in val:
		gpio.output(fcom, gpio.LOW)
		gpio.output(bcom, gpio.LOW)
		gpio.output(rcom, gpio.HIGH)
		gpio.output(lcom, gpio.LOW)
		return
	if 'L' in val:
		gpio.output(fcom, gpio.LOW)
		gpio.output(bcom, gpio.LOW)
		gpio.output(rcom, gpio.LOW)
		gpio.output(lcom, gpio.HIGH)
		return
	if 'D' in val:
		gpio.output(fcom, gpio.HIGH)
		gpio.output(bcom, gpio.LOW)
		gpio.output(rcom, gpio.HIGH)
		gpio.output(lcom, gpio.LOW)
		return
	if 'G' in val:
		gpio.output(fcom, gpio.LOW)
		gpio.output(bcom, gpio.HIGH)
		gpio.output(rcom, gpio.HIGH)
		gpio.output(lcom, gpio.LOW)
		return
	if 'H' in val:
		gpio.output(fcom, gpio.HIGH)
		gpio.output(bcom, gpio.LOW)
		gpio.output(rcom, gpio.LOW)
		gpio.output(lcom, gpio.HIGH)
		return
	if 'J' in val:
		gpio.output(fcom, gpio.LOW)
		gpio.output(bcom, gpio.HIGH)
		gpio.output(rcom, gpio.LOW)
		gpio.output(lcom, gpio.HIGH)
		return

	print "Warning : Invalid order!!!\a\n"
	gpio.output(fcom, gpio.LOW)
	gpio.output(bcom, gpio.LOW)
	gpio.output(rcom, gpio.LOW)
	gpio.output(lcom, gpio.LOW)
	return
	########## socket_callback_end

########## main_program_begin
try:
	init_WiRobot()
except KeyboardInterrupt:
	end_WiRobot()
########## main_program_end
