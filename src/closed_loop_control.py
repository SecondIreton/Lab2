import array

class clCont:
    """
    Created on Tue Jan 31 12:44:02 2023

    @author: gabriel, Trevor Foley
    """
    
    def __init__(self, initSet, initKp):
        self.setpoint = initSet
        self.Kp = initKp
        
    def run(self, setpoint, actual):
        PWM = self.Kp * (setpoint - actual)
        if PWM > 100:
            PWM = 100
        elif PWM < -100:
            PWM = -100
    
        return PWM

    def set_setpoint(self, newSetpoint):
        self.setpoint = newSetpoint

    def set_Kp(self, newKp):
        self.Kp = newKp