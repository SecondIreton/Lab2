
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
    new_Kp = True
    while new_Kp == True:
        print('Input Proportional Gain Constant, Kp:')
        Kp = input()
        try:
            Kp = float(Kp)
            new_Kp = False
        except:
            print('Please input a numeric value.')
    cll = clCont(0, Kp)

    for i in range(100):
        #Set Output to full Rev Here
        # OP = SP +
        lvl = cll.run(8000, enc.read())
        moe.set_duty_cycle(lvl)
        utime.sleep_ms(10)
    moe.set_duty_cycle(0)
    cll.printRes()
    
    cll.printRes()
    
if __name__ == "__main__":
    main()