import time

from tango import DeviceProxy
from sardana.macroserver.macro import macro
#from pygame import mixer

@macro()
def diag_in(self):
    """Macro diag_in"""
    
    diag_mirror=DeviceProxy('tango://hertz.nano.lab:10000/reflectometer/PhytronMCC2/motor541_diag_mirror_InOut')
    power_meter=DeviceProxy('tango://hertz.nano.lab:10000/laser/CoherentPEM/2um_power')
    if diag_mirror.position==32000:
        self.output("Diagnostics mirror is already IN")
    else:
        if power_meter.value>2:
            self.output("2µm power is too high >2W !!! Decrease before moving IN the diagnostics mirror")
        else:
            self.output("Moving IN the diagnostics mirror")
            diag_mirror.position=32000
            while diag_mirror.position!=32000:
                time.sleep(1)

@macro()
def diag_out(self):
    """Macro diag_out"""
    
    diag_mirror=DeviceProxy('tango://hertz.nano.lab:10000/reflectometer/PhytronMCC2/motor541_diag_mirror_InOut')
    if diag_mirror.position==0:
        self.output("Diagnostics mirror is already OUT")
    else:
        self.output("Moving OUT the diagnostics mirror")
        diag_mirror.position=0
        while diag_mirror.position!=0:
            time.sleep(1)

@macro()
def lens_in(self):
    """Macro lens_in"""
    
    HHG_lens=DeviceProxy('tango://hertz.nano.lab:10000/reflectometer/PhytronMCC2/motor540_HHG_lens_x_WorkshopLaser')
    if HHG_lens.position==48.0:
        self.output("HHG lens is already IN")
    else:
        self.output("Moving IN the HHG lens")
        HHG_lens.position=48.0
        while HHG_lens.position!=48.0:
            time.sleep(1)

@macro()
def lens_out(self):
    """Macro lens_out"""
    
    HHG_lens=DeviceProxy('tango://hertz.nano.lab:10000/reflectometer/PhytronMCC2/motor540_HHG_lens_x_WorkshopLaser')
    if HHG_lens.position==6.2:
        self.output("HHG lens is already OUT")
    else:
        self.output("Moving OUT the HHG lens")
        HHG_lens.position=6.2
        while HHG_lens.position!=6.2:
            time.sleep(1)
