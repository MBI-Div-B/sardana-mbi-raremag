import time

from tango import DeviceProxy
from sardana.macroserver.macro import macro

@macro()
def probeon(self):
    """Macro probeon"""
    
    Probe=DeviceProxy('tango://hertz.nano.lab:10000/laser/ThorlabsMFF100/probe_shutter')
    if Probe.mffstate==0:
        self.output("Probe shutter is already open")
    else:
        Probe.close()
        time.sleep(.75)
        if Probe.mffstate==0:
            self.output("Probe shutter opened")
        else:
            self.output("Could not open probe shutter")

@macro()
def probeoff(self):
    """Macro probeoff"""
    
    Probe=DeviceProxy('tango://hertz.nano.lab:10000/laser/ThorlabsMFF100/probe_shutter')
    if Probe.mffstate==1:
        self.output("Probe shutter is already closed")
    else:
        Probe.open()
        time.sleep(.75)
        if Probe.mffstate==1:
            self.output("Probe shutter closed")
        else:
            self.output("Could not close probe shutter")

@macro()
def pumpon(self):
    """Macro pumpon"""
    
    Pump=DeviceProxy('tango://hertz.nano.lab:10000/laser/ThorlabsMFF100/pump_shutter')
    if Pump.mffstate==1:
        self.output("Pump shutter is already open")
    else:
        Pump.open()
        time.sleep(.75)
        if Pump.mffstate==1:
            self.output("Pump shutter opened")
        else:
            self.output("Could not open pump shutter")

@macro()
def pumpoff(self):
    """Macro pumpoff"""
    
    Pump=DeviceProxy('tango://hertz.nano.lab:10000/laser/ThorlabsMFF100/pump_shutter')
    if Pump.mffstate==0:
        self.output("Pump shutter is already closed")
    else:
        Pump.close()
        time.sleep(.75)
        if Pump.mffstate==0:
            self.output("Pump shutter closed")
        else:
            self.output("Could not close pump shutter")
