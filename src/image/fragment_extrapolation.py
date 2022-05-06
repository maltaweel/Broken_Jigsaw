'''
Created on 5 May 2022

@author: maltaweel
'''
import cv2
import numpy as np
from imutils import contours


def fragExtract(images):

    for image in images:
        img_gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(img_gray1, 150, 255, cv2.THRESH_BINARY)
        contours2, hierarchy2 = cv2.findContours(thresh1, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
        image_copy2 = image.copy()
        
        cv2.drawContours(image_copy2, contours2, -1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('SIMPLE Approximation contours', image_copy2)
        cv2.waitKey(0)
        image_copy3 = image.copy()
        
        cv2.imshow('CHAIN_APPROX_SIMPLE Point only', image_copy3)
        cv2.waitKey(0)
        cv2.imwrite('contour_point_simple.jpg', image_copy3)
        cv2.destroyAllWindows()
        
  