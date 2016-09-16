import rospy

import cv
import cv2
from cv_bridge import (CvBridge, CvBridgeError)

from sensor_msgs.msg import Image
import std_srvs.srv
from baxter_interface import CameraControllerk

import numpy


class Camera:
    CAM_X_OFFSET = 0.045
    CAM_Y_OFFSET = -0.01
    CAM_CALIB = 0.0025  # in mm

    def __init__(self, camera_name, resolution=(1280, 800)):
        # self._reset_cameras()
        self.resolution = resolution
        self.cv_image = numpy.zeros((resolution[1], resolution[0], 3), numpy.uint8)
        self.camera_name = camera_name + '_hand_camera'
        self.camera = CameraController(self.camera_name)
        self.bridge = CvBridge()

    def cv_image(self):
        return self.cv_image

    def start(self):
        self.camera.resolution = self.resolution
        self.camera.exposure = -1
        self.camera.gain = -1
        self.camera.white_balance_red = -1
        self.camera.white_balance_green = -1
        self.camera.white_balance_blue = -1

        cam_pub = '/cameras/{0}/image'.format(self.camera_name)
        rospy.Subscriber(cam_pub, Image, self._on_got_image)

    def _on_got_image(self, data):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.waitKey(3)

    @staticmethod
    def _reset_cameras():
        reset_srv = rospy.ServiceProxy('cameras/reset', std_srvs.srv.Empty)
        rospy.wait_for_service('cameras/reset', timeout=10)
        reset_srv()