class clCont:
    """
    Created on Tue Jan 31 12:44:02 2023

    @author: gabriel, Trevor Foley
    """

    def __init__(self, initSet, initKp):
        self.setpoint = initSet
        self.Kp = initKp
        
    def run(self, setpoint, output):
        PWM = self.Kp * (setpoint - output)
        return PWM

    def set_setpoint(self, newSetpoint):
        self.setpoint = newSetpoint

    def set_Kp(self, newKp):
        self.Kp = newKp

