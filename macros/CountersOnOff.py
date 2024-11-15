from sardana.macroserver.macro import macro, Type
    
@macro()
def specon(self):
    """Macro specon"""
    acqConf = self.getEnv('acqConf')
    acqConf['specCCDon'] = True
    self.setEnv('acqConf', acqConf)
    self.info('switching spec CCD counters ON')
    
    # enable spec CCD counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    mnt_grp.setEnabled(True,"spec", "spec1", "spec2", "spec3", "spec4")
    
    if acqConf['altOn']==True:
        mnt_grp.setEnabled(True,"specM", "spec1M", "spec2M", "spec3M", "spec4M")
    
    if acqConf['refOn']==True:
        mnt_grp.setEnabled(True,"specUnpumped", "spec2Unpumped", "spec3Unpumped")
        

@macro()    
def specoff(self):
    """Macro specoff"""
    acqConf = self.getEnv('acqConf')
    acqConf['specCCDon'] = False
    self.setEnv('acqConf', acqConf)
    self.info('switching spec CCD counters OFF')
    
    # disable spec CCD counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    mnt_grp.setEnabled(False,"spec", "spec1", "spec2", "spec3", "spec4", "specM", "spec1M", "spec2M", "spec3M", "spec4M", "specUnpumped", "spec2Unpumped", "spec3Unpumped")
        
@macro()
def refon(self):
    """Macro refon"""
    acqConf = self.getEnv('acqConf')
    acqConf['refCCDon'] = True
    self.setEnv('acqConf', acqConf)
    self.info('switching ref CCD counters ON')
    
    # enable ref CCD counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    mnt_grp.setEnabled(True,"ref", "ref1", "ref2", "ref3", "ref4")
    
    if acqConf['altOn']==True:
        mnt_grp.setEnabled(True,"refM", "ref1M", "ref2M", "ref3M", "ref4M")
    
    if acqConf['refOn']==True:
        mnt_grp.setEnabled(True,"refUnpumped")

@macro()    
def refoff(self):
    """Macro refoff"""
    acqConf = self.getEnv('acqConf')
    acqConf['refCCDon'] = False
    self.setEnv('acqConf', acqConf)
    self.info('switching ref CCD counters OFF')
    
    # disable ref CCD counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    mnt_grp.setEnabled(False,"ref", "ref1", "ref2", "ref3", "ref4", "refM", "ref1M", "ref2M", "ref3M", "ref4M", "refUnpumped")
