import time

from tango import DeviceProxy
from sardana.macroserver.macro import macro

@macro()
def gason(self):
    """Macro gason"""
    
    PressureCtrl=DeviceProxy('tango://hertz.nano.lab:10000/reflectometer/BrooksSLA/HHG_pressure')
    if PressureCtrl.Valve == 0:
        self.output("Gas is already switched ON")
    else:
        PressureCtrl.control()
        time.sleep(1)
        if PressureCtrl.Valve == 0:
            self.output("Gas is now switched ON")
        else:
            self.output("Could not switch on gas")

@macro()
def gasoff(self):
    """Macro gasoff"""
    
    PressureCtrl=DeviceProxy('tango://hertz.nano.lab:10000/reflectometer/BrooksSLA/HHG_pressure')
    if PressureCtrl.Valve == 2:
        self.output("Gas is already switched OFF")
    else:
        PressureCtrl.close()
        time.sleep(1)
        if PressureCtrl.Valve == 2:
            self.output("Gas is now switched OFF")
        else:
            self.output("Could not switch off gas")
