from LimbMover import LimbMover
from Camera import Camera
from LimbRuler import LimbRuler
import cv2
import rospy
import time


lookAt = None



def mouse_callback(event, x, y, flags, param):
    global lookAt
    if event == cv2.EVENT_LBUTTONDOWN:
        lookAt = (x, y)



def to_baxter_coords(px, width, height, cam_calib, dist, cam_x_offset, cam_y_offset, pose):
    x = ((px[1] - (height / 2)) * cam_calib * dist) \
        + pose[0] + cam_x_offset
    y = ((px[0] - (width / 2)) * cam_calib * dist) \
        + pose[1] + cam_y_offset
    return x, y


def draw_aim(image, camera):
    p1 = (camera.resolution[0] / 2, 0)
    p2 = (camera.resolution[0] / 2, camera.resolution[1])
    cv2.line(image, p1, p2, (255, 255, 255))
    cv2.line(image, (0, camera.resolution[1] / 2), (camera.resolution[0], camera.resolution[1] / 2), (255, 255, 255))


def main():
    global lookAt
    rospy.init_node('lookAt')
    camera = Camera('right')
    limb = LimbMover('right')
    ruler = LimbRuler('right')

    cv2.namedWindow('lookAt')
    cv2.setMouseCallback('lookAt', mouse_callback)

    camera.start()

    cz = 0.1
    cx, cy = None, None
    while True:
        image = camera.cv_image
        draw_aim(image, camera)
        cv2.imshow('lookAt', image)

        if lookAt is not None:
            dist = ruler.distance()
            if dist > 65:
                dist = 0.35
            x, y = to_baxter_coords(lookAt, camera.resolution[0],
                                    camera.resolution[1],
                                    camera.CAM_CALIB, dist,
                                    camera.CAM_X_OFFSET,
                                    camera.CAM_Y_OFFSET, limb.pose)
            cx, cy = x, y

            if not limb.move([x, y, cz, -3.1415, 0, 0], move=True):
                print 'cannot moving to', x, y, dist
            else:

                print 'moved to', x, y, dist
            lookAt = None
        key = cv2.waitKey(50) & 0xFF
        if key == 27:
            break
        elif key == ord('s'):
            z = cz + 0.4
            while z > cz and not limb.move([cx, cy, cz + 0.4, -3.1415, 0, 0], move=True):
                z -= 0.05
            limb.move([cx, cy, cz + 0.4, -3.1415, -3.14/2, 0], move=True)
            print limb.move([cx, cy, cz, -3.1415, -3.1415/2, 0], move=True)
        elif key == ord('a'):
            limb.move([cx, cy, cz + 0.4, -3.1415, -3.14/2, 0], move=True)
            limb.move([cx, cy, cz + 0.4, -3.1415, 0, 0], move=True)
            print limb.move([cx, cy, cz, -3.1415, 0, 0], move=True)
        elif key == ord('n'):
            limb.limb_interface.move_to_neutral()



main()