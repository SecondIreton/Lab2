"""!
@file main.py
This file contains code which runs the motor driver, encoder reader, and closed loop controller code
by taking in a proportional gain constant, Kp.

@author mecha12
@date   31-jan
"""

import pyb # The module for the microcontroller
import utime # The internal time module on the microcontroller
from closed_loop_control import clCont # The closed loop control method from closed_loop_control.py
from motor_driver import MotorDriver # The method to drive the motor from motor_drive.py
from encoder_reader import EncoderReader # Read encoder method from encoder_reader.py


def main():
    """!
    Runs the motor by with a proportional gain constant, Kp
    """
    pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    tim = 3
    moe = MotorDriver(pinA10,pinB4,pinB5,tim)
    
    ''' Encoder Setup Below'''
    pinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    enc = EncoderReader(pinB6, pinB7, 4)
    enc.zero()
    
    '''Control Loop Setup'''
    Kp = 0.005 #0.1 excessive oscillation,  0.005 good performance, 0.002 underdamped
    cll = clCont(0, Kp)
    
    '''Serial Bus Setup'''
    ser = pyb.UART(2,115200)

    zeroPoint = utime.ticks_ms() # Initializes the timing scheme
    
    '''Sends time and position datat over the serial port'''
    for i in range(300):
        t = utime.ticks_ms() - zeroPoint
        p = enc.read()
        ser.write(f"{t},{p} \r\n")
        lvl = cll.run(8000, p)
        moe.set_duty_cycle(lvl)
        utime.sleep_ms(10)
    moe.set_duty_cycle(0)
    ser.write("Stahp\r\n")
    
if __name__ == "__main__":
    main()