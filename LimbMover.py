import IKsolver
import baxter_interface


class LimbMover:
    def __init__(self, limb):
        self.limb = baxter_interface.Limb(limb)
        self.ik_solver = IKsolver.IKsolver(limb)

    def move(self, pos):
        point = Point(
            x=pos[0],
            y=pos[1],
            z=pos[2]
        )
        suc = self.ik_solver.solve(point, 'DOWN')
        if suc:
            print 'moving...'
            limb.set_position(self.ik_solver.solution)
        else:
            print 'not moving'






