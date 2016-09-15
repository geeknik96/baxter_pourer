import rospy
import LimbMover
import Camera

def move_arms_to_work_pose(llimb, rlimb):
    llimb.move((0.7, 0.4, -0.5))
    # rlimb.move((0.5, 0.2, 0.3))


def main():
    rospy.init_node('pourer')

    left_limb = LimbMover.LimbMover('left')
    right_limb = LimbMover.LimbMover('right')

    left_camera = Camera.Camera('left')
    right_camera = Camera.Camera('right')

    move_arms_to_work_pose(left_limb, right_limb)

    pass

if __name__ == '__main__':
    main()
