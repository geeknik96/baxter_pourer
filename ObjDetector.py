import cv2
import numpy

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

class ObjDetector:
    def __init__(self):
        self.image = None

        pass

    def set_image(self, image):
        self.image = image

    def detect(self):
        if None:
            print 'set image first!'
            return 0, 0, 0, 0
        x = 0
        y = 0
        w = 10
        h = 10
        tmp = cv2.threshold(self.image, 180, 255, cv2.THRESH_BINARY)
        canny =  tmp[1]
        cv2.imshow('canny', canny)
        return x, y, w, h