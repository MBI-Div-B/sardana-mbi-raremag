from sardana.pool.controller import PseudoCounterController, Type, MaxDimSize
from PyTango import DeviceProxy
import numpy as np

class PumpRefOn2DPseudoCounterController(PseudoCounterController):
    counter_roles        = ('I',)
    pseudo_counter_roles = ('O',)
    value = np.zeros((2048,2048))
    
    def __init__(self, inst, props, *args, **kwargs):
        PseudoCounterController.__init__(self,inst,props, *args, **kwargs)
        self.PumpShutter = DeviceProxy('tango://hertz.nano.lab:10000/laser/ThorlabsMFF100/pump_shutter')
        
    def GetAxisAttributes(self, axis):
        axis_attrs = PseudoCounterController.GetAxisAttributes(self, axis)
        axis_attrs = dict(axis_attrs)
        axis_attrs['Value'][Type] = ((float, ), )
        axis_attrs['Value'][MaxDimSize] = (2048,2048)
        return axis_attrs
    
    def Calc(self, axis, counters):
        counter = counters[0]
        try:
            if self.PumpShutter.mffstate==0:
                self.value = counter
        except:
            pass
        
        return self.value

    def GetAxisPar(self, axis, par):
        if par == "shape":
            return [self.value.shape[0],self.value.shape[1]]
