from sardana.macroserver.macro import imacro, Type, Optional, macro
from sardana.macroserver.scan import *

@macro([
    ["motor", Type.String, None, "Moveable to move"],
    ["start_pos", Type.Float, None, "Scan start position"],
    ["final_pos", Type.Float, None, "Scan final position"],
    ["nr_interv", Type.Integer, None, "Number of scan intervals"],
    ["integ_time", Type.Float, None, "Integration time"]
    ])
def ascan_return(self, motor, start_pos, final_pos, nr_interv, integ_time):
    """runs an ascan and afterwards returns the motor back to its initial position"""

    motor_object = self.getMotion([motor])
    old_position = motor_object.readPosition(force=True)

    scan, _ = self.createMacro('ascan', motor, start_pos, final_pos, nr_interv, integ_time)
    self.runMacro(scan) 

    motor_object.move(old_position)
