from sardana.pool.controller import PseudoMotorController

class TransRotPseudoMotorController(PseudoMotorController):
    """A Slit pseudo motor controller for handling gap and offset pseudo 
       motors. The system uses to real motors sl2t (top slit) and sl2b (bottom
       slit)."""
        
    motor_roles = ('A','B',)
    pseudo_motor_roles = ('trans','rot',)
        
    def __init__(self, inst, props):  
        PseudoMotorController.__init__(self, inst, props)
    
    def CalcPhysical(self, axis, pseudo_pos, curr_physical_pos):
        old_trans = (curr_physical_pos[0]+curr_physical_pos[1])/2
        old_rot = (curr_physical_pos[0]-curr_physical_pos[1])
        move_trans = pseudo_pos[0]-old_trans
        move_rot = (pseudo_pos[1]-old_rot)/2
        if axis == 1:
            return curr_physical_pos[0]+move_trans+move_rot
        else:
            return curr_physical_pos[1]+move_trans-move_rot
            
    
    def CalcPseudo(self, axis, physical_pos, curr_pseudo_pos):
        if axis == 1:
            return (physical_pos[0]+physical_pos[1])/2
        else:
            return (physical_pos[0]-physical_pos[1])
        
