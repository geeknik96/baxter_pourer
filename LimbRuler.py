from baxter_interface import AnalogIO
import sys


class LimbRuler:
    def __init__(self, limb):
        self.limb = limb
        self.analog_io = '{0}_hand_range'.format(limb)
        self.ruler = AnalogIO(self.analog_io)
        self.value = None

    def distance(self):
        dist = self.ruler.state()
        if dist > 65000 and not self.value:
            return 0.2
        self.value = float(dist / 1000)
        return self.value
