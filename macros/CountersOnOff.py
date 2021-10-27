from sardana.macroserver.macro import macro, Type

@macro()
def vimbaon(self):
    """Macro vimbaon"""
    self.info('switching Vimba cam counters ON')
    
    # enable vimba counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    mnt_grp.setEnabled(True,"vimba", "vimba1", "vimba2")

@macro()    
def vimbaoff(self):
    """Macro vimbaoff"""
    self.info('switching Vimba cam counters OFF')
    
    # disable vimba counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    mnt_grp.setEnabled(False,"vimba", "vimba1", "vimba2")
    
@macro()
def specon(self):
    """Macro specon"""
    self.info('switching SPEC cam counters ON')
    
    # enable spec counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    acqConf = self.getEnv('acqConf')
    if acqConf['altOn']==False:
        mnt_grp.setEnabled(True,"spec", "spec1", "spec2", "spec3", "spec4")
    else:
        mnt_grp.setEnabled(True,"spec", "specM", "spec1", "spec1M", "spec2", "spec2M", "spec3", "spec3M", "spec4", "spec4M")

@macro()    
def specoff(self):
    """Macro specoff"""
    self.info('switching SPEC cam counters OFF')
    
    # disable spec counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    acqConf = self.getEnv('acqConf')
    if acqConf['altOn']==False:
        mnt_grp.setEnabled(False,"spec", "spec1", "spec2", "spec3", "spec4")
    else:
        mnt_grp.setEnabled(False,"spec", "specM", "spec1", "spec1M", "spec2", "spec2M", "spec3", "spec3M", "spec4", "spec4M")
        
@macro()
def refon(self):
    """Macro refon"""
    self.info('switching REF cam counters ON')
    
    # enable spec counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    acqConf = self.getEnv('acqConf')
    if acqConf['altOn']==False:
        mnt_grp.setEnabled(True,"ref", "ref1", "ref2", "ref3", "ref4")
    else:
        mnt_grp.setEnabled(True,"ref", "refM", "ref1", "ref1M", "ref2", "ref2M", "ref3", "ref3M", "ref4", "ref4M")

@macro()    
def refoff(self):
    """Macro refoff"""
    self.info('switching REF cam counters OFF')
    
    # disable spec counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    
    acqConf = self.getEnv('acqConf')
    if acqConf['altOn']==False:
        mnt_grp.setEnabled(False,"ref", "ref1", "ref2", "ref3", "ref4")
    else:
        mnt_grp.setEnabled(False,"ref", "refM", "ref1", "ref1M", "ref2", "ref2M", "ref3", "ref3M", "ref4", "ref4M")