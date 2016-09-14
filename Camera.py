import cv2
import cv2_bridge

from sensor_msgs.msg import Image

class Camera:
    def __init__(self, camera):
        self.frame = None
        cam_pub = "/cameras/{0}/image" % camera

        self.cam = rospy.Subscriber(cam_pub, Image, self._on_got_image)
        pass

    def _on_got_image(self, msg):
        self.frame = msg_to_cv(msg)

    def currentFrame(self):
        return self.frame