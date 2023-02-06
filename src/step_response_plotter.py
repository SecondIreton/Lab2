#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:56:44 2023

@author: scottbrown
"""

# Import serial library
import serial
# Import pyplot
from matplotlib import pyplot

# Create empty lists of x and y data
x_data = []
y_data = []

# Create labels for plots
x_label = 'Time, s'  ## Variable name
y_label = 'Location, ticks'  ## Variable name

req_point =  input('Enter a 4 digit number: ')
if req_point.type == int():
    setpoint = req_point  # Assign the inputed value to setpoint
    
# The shoe serial port for the mac: /dev/tty.usbmodem2073337757522

with serial.Serial() as s_port: # Fill in correct serial port when found
    
    s_port.write (setpoint) # Send the set point value
    
    entry = s_port.readline().split(b' , ')
    print(entry) # Test to see if we have the correct inputs
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