from sardana.macroserver.macro import macro, Type

@macro()
def pumprefon(self):
    """Macro refon"""
    acqConf = self.getEnv('acqConf')
    acqConf['refOn'] = True
    self.setEnv('acqConf', acqConf)
    self.info('switching reference ON')
    
    # enable reference counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    # mnt_grp.setEnabled(True, "specM", "spec1M", "spec2M", "spec3M", "spec4M")#,"refM", "ref1M", "ref2M", "ref3M", "ref4M")


@macro()    
def pumprefoff(self):
    """Macro refoff"""
    acqConf = self.getEnv('acqConf')
    acqConf['refOn'] = False
    self.setEnv('acqConf', acqConf)
    self.info('switching reference OFF')
    
    # disable reference counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    # mnt_grp.setEnabled(False, "specM", "spec1M", "spec2M", "spec3M", "spec4M")#, "refM", "ref1M", "ref2M", "ref3M", "ref4M")
    
