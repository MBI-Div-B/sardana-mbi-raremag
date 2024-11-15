from sardana.pool.controller import PseudoCounterController, Type, MaxDimSize
from PyTango import DeviceProxy
import numpy as np

class PumpRefOn0DPseudoCounterController(PseudoCounterController):
    counter_roles        = ('I',)
    pseudo_counter_roles = ('O',)
    value = 0
    
    def __init__(self, inst, props, *args, **kwargs):
        PseudoCounterController.__init__(self,inst,props, *args, **kwargs)
        self.PumpShutter = DeviceProxy('tango://hertz.nano.lab:10000/laser/ThorlabsMFF100/pump_shutter')
            
    def Calc(self, axis, counters):
        counter = counters[0]
        try:
            if self.PumpShutter.mffstate==0:
                self.value = counter
        except:
            pass
        
        return self.value
