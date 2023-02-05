import array
import utime

class clCont:
    """
    Created on Tue Jan 31 12:44:02 2023

    @author: gabriel, Trevor Foley
    """
    
    def __init__(self, initSet, initKp):
        self.setpoint = initSet
        self.Kp = initKp
        self.t = array.array('I', [])
        self.p = array.array('I', [])
        
    def run(self, setpoint, actual):
        PWM = self.Kp * (setpoint - actual)
        if PWM > 100:
            PWM = 100
        elif PWM < -100:
            PWM = -100
        return PWM
    
        self.t.append(utime.ticks_ms())
        self.p.append(actual)

    def set_setpoint(self, newSetpoint):
        self.setpoint = newSetpoint

    def set_Kp(self, newKp):
        self.Kp = newKp

    def printRes(self):
        for val in len(self.t):
            print(self.t[val], ",", self.p[val])
            