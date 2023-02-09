#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:56:44 2023
@author: scottbrown
@title: step_response_plotter
"""

# Import serial library
import serial
# Import pyplot
from matplotlib import pyplot

# Create empty lists of x and y data
x_data = []
y_data = []

# Create labels for plots
x_label = 'Time, ms'  ## Variable name
y_label = 'Location, ticks'  ## Variable name

# The shoe serial port for the mac: /dev/tty.usbmodem2073337757522
# for max COM: '/dev/cu.usbmodem103'

with serial.Serial('COM11',115200) as s_port: # Fill in correct serial port when found
    s_port.flush()
    #s_port.write(setpoint) # Send the set point value
    
    '''req_point =  input('Enter a Kp Value: ')
    if type(req_point) == float():
        Kp_Val = float(req_point)
        s_port.write(b'Kp_Val')
'''
    #if s_port.any is True:
    while True:
        entry = s_port.readline().decode()
        if entry == 'Stahp\r\n':
            print('dafuq')
            break
        entry = entry.split(',')
        try:    # Check if the values can be converted into a float
            entry[0] = float(entry[0])
            entry[1] = float(entry[1])
            x_data.append(entry[0])
            y_data.append(entry[1])
        except:     # If not a number, skip line
            pass

    
    # Print values into new plot
    pyplot.plot(x_data, y_data)
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.show()