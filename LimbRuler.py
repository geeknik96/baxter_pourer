from baxter_interface import AnalogIO
import sys


class LimbRuler:
    def __init__(self, limb):
        self.limb = limb
        self.analog_io = '{0}_hand_range'.format(limb)
        self.ruler = AnalogIO(self.analog_io)

    def distance(self):
        dist = self.ruler.state()
        # if dist > 65000:
        #     sys.exit("ERROR - get_distance - no distance found")
        return float(dist / 1000)  # in mm
