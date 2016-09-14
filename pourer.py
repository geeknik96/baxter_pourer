import LimbMover
import Camera

def move_arms_to_work_pose(llimb, rlimb):
    llimb.move((0, 0, 0))
    rlimb.move((0, 0, 0))


def main():
    left_limb = LimbMover('left')
    right_limb = LimbMover('right')

    left_camera = Camera('left')
    right_camera = Camera('right')

    pass

if __name__ == '__main__':
    main()
