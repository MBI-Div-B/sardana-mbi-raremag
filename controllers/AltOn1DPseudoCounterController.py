from sardana.pool.controller import PseudoCounterController, Type, MaxDimSize
from PyTango import DeviceProxy
import numpy as np

class AltOn1DPseudoCounterController(PseudoCounterController):
    """ A  pseudo counter which remebers the input for negative magnetic
    fields and returns it at positive fields"""

    counter_roles        = ('I',)
    pseudo_counter_roles = ('O',)
    spectrum = np.zeros((2048,))
    field = 0
    
    def __init__(self, inst, props, *args, **kwargs):
        PseudoCounterController.__init__(self,inst,props, *args, **kwargs)
        #self.magnetState = DeviceProxy("raremag/MagnetState/magnet")
        self.magnet = DeviceProxy("tango://hertz.nano.lab:10000/reflectometer/KepcoSerialGPIB/magnet")
        
    def GetAxisAttributes(self, axis):
        axis_attrs = PseudoCounterController.GetAxisAttributes(self, axis)
        axis_attrs = dict(axis_attrs)
        axis_attrs['Value'][Type] = (float, )
        axis_attrs['Value'][MaxDimSize] = self.spectrum.shape
        return axis_attrs
    
    def Calc(self, axis, counters):
        counter = counters[0]
        try:
            #self.field = self.magnetState.magnet
            self.field = self.magnet.current
            
            if self.field < 0:
                self.spectrum = np.sum(counter, axis=0)
        except:
            pass
        
        return self.spectrum

    def GetAxisPar(self, axis, par):
        if par == "shape":
            return [self.spectrum.shape[0]]
