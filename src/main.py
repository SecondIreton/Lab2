
"""
Created on Tue Jan 31 13:18:54 2023

@author: gabri
"""
    
import pyb
import utime
import cLCont
import MotorDriver
import EncoderReader

def main():
    ''' Motor Setup Below'''
    pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    tim = 3
    moe = MotorDriver(pinA10,pinB4,pinB5,tim)
    
    clCont.set_setpoint(0)
    while(True):
        utime.sleep_ms(10)
        cLCont.set_setpoint()
        cLCont.set_Kp()
    
