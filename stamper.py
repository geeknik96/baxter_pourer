import cv2
import time
import random
import rospy
from Camera import Camera
from LimbMover import LimbMover
from LimbRuler import LimbRuler
from TemplateMatcher import TemplateMatcher


class Stamper:
    aim_x = 546.0 / 960.0
    aim_y = 244.0 / 600.0

    def __init__(self, paths):
        self.stamp_finder = self._create_matchers(paths)

        self.camera = Camera('left')
        self.camera.start()
        self.limb = LimbMover('left')
        self.ruler = LimbRuler('left')

    def _to_baxter_coords(self, px):
        dist = self.ruler.distance()
        cam_calib = self.camera.CAM_CALIB
        cam_x_offset = self.camera.CAM_X_OFFSET
        cam_y_offset = self.camera.CAM_Y_OFFSET
        width, height = self.camera.resolution
        pose = self.limb.pose

        x = ((px[1] - (height / 2)) * cam_calib * dist) \
            + pose[0] + cam_x_offset
        y = ((px[0] - (width / 2)) * cam_calib * dist) \
            + pose[1] + cam_y_offset

        return x, y

    def _move_to(self, x, y):
        rx, ry = self._to_baxter_coords((x, y))
        pose = self.limb.pose
        pose[0] = rx
        pose[1] = ry
        if not self.limb.move(pose, move=True):
            print 'cannot move'


    @staticmethod
    def _create_matchers(paths):
        matchers = []
        for tmpl in paths:
            image = cv2.imread(tmpl)
            mather = TemplateMatcher(image)
            matchers.append(mather)
        return matchers

    def find_stamp(self):
        result = 0, 0, 0, 0
        matchers = self.stamp_finder

        def area(rect):
            w = (rect[2] - rect[0])
            h = (rect[3] - rect[1])
            return w * h
        for mather in matchers:
            mather.set_image(self.camera.cv_image)
            res = mather.match()
            if area(res) > area(result):
                result = res
        return result

    def draw_aim(self, image):
        camera = self.camera
        aim_x = self.aim_x
        aim_y = self.aim_y
        p1 = (aim_x * camera.resolution[0], 0)
        p2 = (aim_x * camera.resolution[0], camera.resolution[1])
        p3 = (0, aim_y * camera.resolution[1])
        p4 = (camera.resolution[0], aim_y * camera.resolution[1])
        cv2.line(image, p1, p2, (255, 255, 255))
        cv2.line(image, p3, p4, (255, 255, 255))

    def aim_to_stamp(self):
        cx = self.aim_x * self.camera.resolution[0]
        cy = self.aim_y * self.camera.resolution[1]

        def find_aim(this):
            for _ in range(10):
                obj_rect = this.find_stamp()
                if all(obj_rect) is 0:
                    cv2.waitKey(100)
                return obj_rect
            return False

        obj_rect = find_aim(self)
        if not obj_rect:
            print 'not find stamp'
            return False

        obj_x = (obj_rect[2] - obj_rect[0]) / 2
        obj_y = (obj_rect[3] - obj_rect[1]) / 2

        self._move_to(obj_x, obj_y)



def main():
    rospy.init_node('stamper')

    paths = ['images/stamp{0}.png'.format(i) for i in range(1, 5)]
    stamper = Stamper(paths)
    while True:
        stamper.aim_to_stamp()
        cv2.imshow('stamter', stamper.camera.cv_image)
        cv2.waitKey(1000)

if __name__ == '__main__':
    main()





