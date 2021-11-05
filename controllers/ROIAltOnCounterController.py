##############################################################################
##
# This file is part of Sardana
##
# http://www.sardana-controls.org/
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Sardana is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Sardana is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Sardana.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

"""This module contains the definition of a I/I0 pseudo counter controller
for the Sardana Device Pool"""

__all__ = ["ROIAltOnCounterController"]

__docformat__ = 'restructuredtext'

from sardana.pool.controller import PseudoCounterController
from sardana import DataAccess
from sardana.pool.controller import Type, Description, Access, DefaultValue
from sardana.pool.controller import Memorized, Memorize
import numpy as np
from PyTango import DeviceProxy

class ROIAltOnCounterController(PseudoCounterController):
    """ A simple pseudo counter which receives two counter values (I and I0)
        and returns I/I0"""

    counter_roles = ('image',)
    pseudo_counter_roles = ('roi1', 'roi2', 'roi3', 'roi4', 'roi1M', 'roi2M', 'roi3M', 'roi4M', )
    value = [0, 0, 0, 0]
    field = 0

    ctrl_attributes = {
    "rois" : {
            Type         : (int,),
            Description  : "List of ROIs",
            Access : DataAccess.ReadWrite,
            DefaultValue : [0, -1, 0, -1],
            Memorized: Memorize,
        },
    }
    
    def __init__(self, inst, props, *args, **kwargs):
        """Constructor"""
        PseudoCounterController.__init__(self,inst,props, *args, **kwargs)
        self.magnetState = DeviceProxy("raremag/MagnetState/magnet")

        
    def Calc(self, axis, counter_values):
        image = np.array(counter_values[0])
        
        if axis > 4:
            ax = axis - 5
        else:
            ax = axis - 1
            
        try:
            roi = np.s_[self._rois[0+4*ax]:self._rois[1+4*ax],
                        self._rois[2+4*ax]:self._rois[3+4*ax]]
            value =  image[roi].sum()
        except IndexError:
            value =  -1
        except AttributeError:
            value = -2
        
        if axis > 4:       
            try:
                self.field = self.magnetState.magnet
                
                if self.field < 0:
                    self.value[ax] = value
            except:
                pass
            
            return self.value[ax]
        else:
            return value
