import IKSolver
import baxter_interface

from geometry_msgs.msg import (
    Point)



class LimbMover:
    def __init__(self, limb):
        self.limb = baxter_interface.Limb(limb)
        self.ik_solver = IKSolver.IKsolver(limb)

    def move(self, pos):
        point = Point(
            x=pos[0],
            y=pos[1],
            z=pos[2]
        )
        suc = self.ik_solver.solve(point, 'FRONT')
        if suc:
            print 'moving...'
            self.limb.move_to_joint_positions(self.ik_solver.solution)
        else:
            print 'not moving'






