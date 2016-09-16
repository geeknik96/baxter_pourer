import rospy
import LimbMover
import Camera
import random
import time

def move_arms_to_work_pose(llimb, rlimb):
    llimb.move((0.7, 0.0, 0.08))
    rlimb.move((0.5, 0.2, 0.3))


def main():
    rospy.init_node('pourer')

    left_limb = LimbMover.LimbMover('left')
    # right_limb = LimbMover.LimbMover('right')

    left_camera = Camera.Camera('left')
    left_camera.start()
    # right_camera = Camera.Camera('right')

    left_limb.limb_interface.set_joint_position_speed(1.0)
    # right_limb.limb_interface.set_joint_position_speed(1.0)
    x = 0.4
    while x < 0.8:
        y = 0.4
        while y < 0.6:
            w = random.random() * 3.14
            print x, y, w
            left_limb.move([x, y, 0.15, -3.14, 0, w])
            img = left_camera.cv_image
            Camera.cv2.imshow('vision', img)
            Camera.cv2.waitKey(2000)
            # right_limb.move([x, y - 0.3, 0.15, -3.14, 0, w])
            y += 0.05
        x += 0.1
    pass

if __name__ == '__main__':
    main()
