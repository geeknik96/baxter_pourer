import baxter_interface

class LimbRuler:
    def __init__(self, limb):
        self.limb = limb
        self.ruler = baxter_interface.analog_io.AnalogIO('{0}_hand_range' % limb)

    def distance(self):
        dist = ruler.state()
        if dist > 65000:
            sys.exit("ERROR - get_distance - no distance found")
        return float(dist / 1000) # in mm
