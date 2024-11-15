from sardana.macroserver.macro import macro, Type

@macro()
def securityon(self):
    """Macro securityon"""
    acqConf = self.getEnv('acqConf')
    acqConf['securityOn'] = True
    self.setEnv('acqConf', acqConf)
    self.info('switching security measures ON')

@macro()    
def securityoff(self):
    """Macro securityoff"""
    acqConf = self.getEnv('acqConf')
    acqConf['securityOn'] = False
    self.setEnv('acqConf', acqConf)
    self.info('switching security measures OFF')