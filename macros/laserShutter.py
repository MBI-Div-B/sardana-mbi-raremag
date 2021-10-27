import time

from tango import DeviceProxy
from sardana.macroserver.macro import macro

@macro()
def ProbeOn(self):
    """Macro ProbeOn"""
    
    Probe=DeviceProxy('raremag/ThorlabsMFF102/flip01')
    if Probe.isClose:
        self.output("Probe shutter is already open")
    else:
        Probe.close()
        time.sleep(1)
        if Probe.isClose:
            self.output("Probe shutter opened")
        else:
            self.output("Could not open Probe shutter")

@macro()
def ProbeOff(self):
    """Macro ProbeOff"""
    
    Probe=DeviceProxy('raremag/ThorlabsMFF102/flip01')
    if Probe.isOpen:
        self.output("Probe shutter is already closed")
    else:
        Probe.open()
        time.sleep(1)
        if Probe.isOpen:
            self.output("Probe shutter closed")
        else:
            self.output("Could not close Probe shutter")

@macro()
def PumpOn(self):
    """Macro PumpOn"""
    
    Pump=DeviceProxy('raremag/ThorlabsMFF102/flip02')
    if Pump.isOpen:
        self.output("Pump shutter is already open")
    else:
        Pump.open()
        time.sleep(1)
        if Pump.isOpen:
            self.output("Pump shutter opened")
        else:
            self.output("Could not open Pump shutter")

@macro()
def PumpOff(self):
    """Macro PumpOff"""
    
    Pump=DeviceProxy('raremag/ThorlabsMFF102/flip02')
    if Pump.isClose:
        self.output("Pump shutter is already closed")
    else:
        Pump.close()
        time.sleep(1)
        if Pump.isClose:
            self.output("Pump shutter closed")
        else:
            self.output("Could not close Pump shutter")