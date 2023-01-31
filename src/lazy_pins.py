import pyb
class lazyPins:
    """
    Created on Tue Jan 31 14:10:07 2023
    
    @author: gabri
    """
    
    def __init__(self, pin, direction):
        #pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
        setPin = pyb.Pin(pyb.Pin.board.pin,pyb.Pin.direction)
        return setPin
