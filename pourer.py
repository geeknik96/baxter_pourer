import rospy
import LimbMover
import Camera
import random
import LimbRuler
import TemplateMatcher
import time


def main():
    rospy.init_node('pourer')

    left_limb = LimbMover.LimbMover('left')
    # right_limb = LimbMover.LimbMover('right')

    # left_camera = Camera.Camera('left')
    # left_camera.start()
    # limb_ruler = LimbRuler.LimbRuler('left')
    # detector = ObjDetector.ObjDetector()
    # right_camera = Camera.Camera('right')

    left_limb.limb_interface.set_joint_position_speed(1.0)
    # right_limb.limb_interface.set_joint_position_speed(1.0)
    x = 0.4
    while x < 0.8:
        y = 0.4
        while y < 0.6:
            w = random.random() * 3.14
            print x, y, w
            left_limb.move([x, y, 0.15, -3.14, -3.14/2, 0], move=True)
            # right_limb.move([x, y - 0.3, 0.15, -3.14, 0, w])
            y += 0.05
        x += 0.1
    pass

if __name__ == '__main__':
    main()
