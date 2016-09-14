import cv2
import rospy
from baxter_interface import (
    Limb,
    Head,
    Gripper,
    RobotEnable,
    CameraController )

import cv2
import cv_bridge

from sensor_msgs.msg import (
    Image, Range
)

rospy.init_node('BaxterCooker')
baxter = RobotEnable()

image = 0

xdisp = rospy.Publisher('/robot/xdisplay', Image, latch=True)

rate = rospy.Rate(1)
def sendImage(msg):
    xdisp.publish(msg)

# def printRange(msg):
#     print msg

lcam = rospy.Subscriber("/cameras/left_hand_camera/image", Image, sendImage)
# range = rospy.Subscriber("/robot/range/right_hand_range/range", Range, printRange)

while True:
    rate.sleep()


print '1'



#
#
# right_arm = Limb('right')
# left_arm = Limb('left')
# right_arm.move_to_neutral()
# left_arm.move_to_neutral()
#
# right_gripper = Gripper('right')
# left_gripper = Gripper('left')
#
# left_hand_camera = CameraController('left_hand_camera')
# right_hand_camera = CameraController('right_hand_camera')
# # head_camera = CameraController('head_camera')
#

