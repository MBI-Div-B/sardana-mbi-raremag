from sardana.macroserver.macro import Macro, Hookable, Type, Optional, macro
from PyTango import DevState
import logging

class cte_old(Macro, Hookable):

    hints = {'allowsHooks': ('pre-acq', 'post-acq')}
    param_def = [
        ['integ_time', Type.Float, 1.0, 'Integration time'],
        ['countable_elem', Type.Countable, Optional,
         'Countable element e.g. MeasurementGroup or ExpChannel']
    ]

    def prepare(self, integ_time, countable_elem, **opts):
        if countable_elem is None:
            try:
                self.countable_elem_name = self.getEnv('ActiveMntGrp')
            except UnknownEnv:
                return
        else:
            self.countable_elem_name = countable_elem.name
        self.countable_elem = self.getObj(self.countable_elem_name)

    def run(self, integ_time, countable_elem):
        if self.countable_elem is None:
            msg = ('Unknown countable {0} element. Use macro parameter or'
                   'ActiveMntGrp environment variable'.format(
                                                    self.countable_elem_name))
            self.error(msg)
            return
        # integration time has to be accessible from with in the hooks
        # so declare it also instance attribute
        self.integ_time = integ_time
        self.outputDate()
        self.outputBlock('Continuous run...')
        self.flushOutput()
        __iteration = 0

        while 1:
            for preAcqHook in self.getHooks('pre-acq'):
                preAcqHook()

            try:
                state, data = self.countable_elem.count(integ_time)
            except Exception:
                if self.countable_elem.type == Type.MeasurementGroup:
                    names = self.countable_elem.ElementList
                    elements = [self.getObj(name) for name in names]
                    self.dump_information(elements)
                raise
            if state != DevState.ON:
                if self.countable_elem.type == Type.MeasurementGroup:
                    names = self.countable_elem.ElementList
                    elements = [self.getObj(name) for name in names]
                    self.dump_information(elements)
                    raise ValueError("Acquisition ended with {}".format(
                        state.name.capitalize()))

            for postAcqHook in self.getHooks('post-acq'):
                postAcqHook()

            __iteration += 1
            self.outputBlock('Continuous run... %d' % __iteration)

@macro([["integ_time", Type.Float, 1.0, "Integration time"]])
def cte(self, integ_time):
    """Continuous ct loop"""

    ct, _ = self.createMacro('ct', integ_time)
    ct.log_obj.setLevel(logging.ERROR)

    self.outputDate()
    self.outputBlock('Continuous run...')
    __iteration = 0

    while True:
        self.runMacro(ct)
        __iteration += 1
        self.outputBlock('Continuous run... %d' % __iteration)
