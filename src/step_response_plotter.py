"""!
@file step_response_plotter.py
This file contains code which takes in time and position data from the serial port
and outputs plots of the time and position

@author mecha12
@date   31-jan
"""

import serial # Import serial library
from matplotlib import pyplot # Import pyplot

# Create empty lists of x and y data
x_data = []
y_data = []

# Create labels for plots
x_label = 'Time, ms'  ## Variable name
y_label = 'Location, ticks'  ## Variable name

with serial.Serial('COM11',115200) as s_port: # Fill in correct serial port when found
    s_port.flush() # Clear serial port
    
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