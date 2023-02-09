"""
Created on Tue Jan 31 13:18:54 2023

@author: gabri
"""
    
import pyb
import utime
from closed_loop_control import clCont
from motor_driver import MotorDriver
from encoder_reader import EncoderReader
#import clCont
#import MotorDriver
#import EncoderReader
#from lazy_pins import lazyPins

def main():
    ''' Motor Setup Below'''
    pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    #pinA10 = lazyPins('PA10','OUT_PP')
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
    Kp = 0.005				#0.1 excessive oscillation,  0.005 good performance, 0.002 underdamped
    cll = clCont(0, Kp)
    
    '''Serial Bus Setup'''
    ser = pyb.UART(2,115200)

    zeroPoint = utime.ticks_ms()
    
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