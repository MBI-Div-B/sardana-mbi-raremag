# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:57:08 2018

@author: korff
"""
from sardana.macroserver.macro import macro, Type
import time
from dirsync import sync
import os
from PyTango import DeviceProxy
import subprocess

@macro()
def userPreAcq(self):
    acqConf  = self.getEnv('acqConf')
    altOn    = acqConf['altOn']
    refOn    = acqConf['refOn']
    waittime = acqConf['waitTime']
    
    if waittime:
        time.sleep(waittime)
        self.debug('waiting for %.2f s', waittime)
        
    if altOn:
        # move magnet to minus amplitude
        magnConf    = self.getEnv('magnConf')
        ampl        = magnConf['ampl']
        magwaittime = magnConf['waitTime']
        magnet      = self.getMotion(["magnet"])
        #magnetState = DeviceProxy('raremag/MagnetState/magnet')
        
        magnet.move(-1*ampl)
        #magnetState.magnet = -1*ampl
        
        self.debug('mag. waiting for %.2f s', magwaittime)
        time.sleep(magwaittime)        
        
        parent = self.getParentMacro()
        if parent:
            integ_time  = parent.integ_time
            mnt_grp     = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
            state, data = mnt_grp.count(integ_time)
                       
        magnet.move(+1*ampl)
        #magnetState.magnet = +1*ampl
        
        self.debug('mag. waiting for %.2f s', magwaittime)
        time.sleep(magwaittime)                
    else:
        pass

    if refOn:
        PumpShutter=DeviceProxy('tango://hertz.nano.lab:10000/laser/ThorlabsMFF100/pump_shutter')

        # close pump shutter
        # print('Closing pump shutter')
        PumpShutter.close()
        time.sleep(0.75)

        parent = self.getParentMacro()
        if parent:
            integ_time  = parent.integ_time
            mnt_grp     = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
            state, data = mnt_grp.count(integ_time)

        # open pump shutter
        # print('Opening pump shutter')
        PumpShutter.open()
        time.sleep(0.75)
    else:
        pass
    
@macro()
def userPreScan(self):
    acqConf  = self.getEnv('acqConf')
    altOn    = acqConf['altOn']
    refOn    = acqConf['refOn']
    
    if altOn or refOn:
        parent = self.getParentMacro()
        if parent:
            parent._gScan.deterministic_scan = False

    pass
    
@macro()
def userPostScan(self):
    scanDir = self.getEnv('ScanDir')
    
    if scanDir != "" and scanDir != None:
        self.output("Mirroring on NAS initiated...")
        result = subprocess.run(
            f'rsync -xa -v --progress {scanDir}/* data_writer@nasbnano.nano.lab:/share/data/reflectometer',
            shell=True,
            stdout=subprocess.PIPE,
        )
        self.output(result.stdout.decode("utf-8"))
        self.output("End of mirroring.")
    else:
        self.output("ScanDir is not set, please check the save path.")
    
@macro()
def userPreMv(self):
    acqConf    = self.getEnv('acqConf')
    securityOn = acqConf['securityOn']

    if securityOn:
        for moveable in self.parent_macro.motors:
            if moveable.name == 'tth':
                ref_x = self.getMotion(["ref_x"])
                #ref_x = self.getMoveables("ref_x")
                if ref_x.readPosition()[0] > 0:
                    self.outputBlock('ref_x needs to be 0.0 before this movement is allowed, press Ctrl+C to abort')
                    #self.outputBlock(str(self.parent_macro.getParameters()))
                    self.parent_macro.stop()
    else:
        self.outputBlock('WARNING! You are about to move motors with security measures turned OFF!')
        time.sleep(5)
        pass
