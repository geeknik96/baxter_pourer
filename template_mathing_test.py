import cv2
import rospy
import time
from Camera import Camera
from TemplateMatcher import TemplateMatcher


def create_template():
    rospy.init_node('template')

    camera = Camera('left')
    camera.start()
    time.sleep(1)

    image = camera.cv_image
    cv2.imwrite('/home/baxter/Projects/baxter_pourer/images/tmp.png', image)


def main():
    rospy.init_node('template_search')

    camera = Camera('left')
    camera.start()

    paths = [
        '/home/baxter/Projects/baxter_pourer/images/stamp1.png',
        '/home/baxter/Projects/baxter_pourer/images/stamp2.png',
        '/home/baxter/Projects/baxter_pourer/images/stamp3.png',
        '/home/baxter/Projects/baxter_pourer/images/stamp4.png',
        '/home/baxter/Projects/baxter_pourer/images/stamp5.png',
    ]

    mathers = []
    for tmpl in paths:
        image = cv2.imread(tmpl)
        mather = TemplateMatcher(image)
        mathers.append(mather)

    while True:
        image = camera.cv_image
        for mather in mathers:
            mather.set_image(image)
            result = mather.match()

            if result[:2] is not [0, 0]:
                cv2.rectangle(image, result[:2], result[2:], (255, 255, 0))
        cv2.imshow('TemplateMatcher', image)
        key = cv2.waitKey(100) & 0xFF
        if key == 27:
            break

if __name__ == '__main__':
    main()
