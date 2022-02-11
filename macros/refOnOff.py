from sardana.macroserver.macro import macro, Type

@macro()
def pumprefon(self):
    """Macro refon"""
    acqConf = self.getEnv('acqConf')
    acqConf['refOn'] = True
    self.setEnv('acqConf', acqConf)
    self.info('switching unpumped reference ON')
    
    # enable reference counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    mnt_grp.setEnabled(True, "dummy2DUnpumped", "epochUnpumped", "thorlabsPM1Unpumped", "ADC0Unpumped", "ADC1Unpumped")


@macro()    
def pumprefoff(self):
    """Macro refoff"""
    acqConf = self.getEnv('acqConf')
    acqConf['refOn'] = False
    self.setEnv('acqConf', acqConf)
    self.info('switching unpumped reference OFF')
    
    # disable reference counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    mnt_grp.setEnabled(False, "dummy2DUnpumped", "epochUnpumped", "thorlabsPM1Unpumped", "ADC0Unpumped", "ADC1Unpumped")
    
