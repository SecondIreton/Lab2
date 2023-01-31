# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:44:02 2023

@author: gabriel, Trevor Foley
"""

class clCont:
    setpoint = 0
    Kp = 0

    def __init__(self, initSet, initKp):
        self.setpoint = initSet
        self.Kp = initKp

    def set_setpoint(self, newSetpoint):
        self.setpoint = newSetpoint

    def set_Kp(self, newKp):
        self.Kp = newKp

