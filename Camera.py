import cv2


from sensor_msgs.msg import Image

class Camera:
    CAM_X_OFFSET = 0.045
    CAM_Y_OFFSET = -0.01
    CAM_CALIB =  0.0025 #in mm
    def __init__(self, camera_name, resolution=(1280, 800)):
        self.frame = None
        cam_nam = '{0}_hand_camera'
        self.camera = baxter_interface.camera.CameraControl('{0}_hand_camera' % camera_name)
        cam_pub = "/cameras/{0}/image" % camera

        self.cam = rospy.Subscriber(cam_pub, Image, self._on_got_image)
        pass

    def start(self):
        rospy.Subscriber()

    def _on_got_image(self, msg):
        self.frame = msg_to_cv(msg)

    def currentFrame(self):
        return self.frame