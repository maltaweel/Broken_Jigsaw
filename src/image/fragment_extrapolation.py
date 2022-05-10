'''
Created on 5 May 2022

@author: maltaweel
'''
import cv2
import os
import numpy as np
from imutils import contours

BLACK_THRESHOLD = 200
THIN_THRESHOLD = 10

#the path to the data folder
pn=os.path.abspath(__file__)
pn=pn.split("src")[0]  
contours_directory=os.path.join(pn,'raw_contours')
total_image=os.path.join(pn,'total_image')
def fragExtract(images):

    idx = 0
    img=0
    for image in images:
        img_gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(img_gray1, 150, 255, cv2.THRESH_BINARY)
        contours2, hierarchy2 = cv2.findContours(thresh1, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
        image_copy2 = image.copy()
        
        cv2.drawContours(image_copy2, contours2, -1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('SIMPLE Approximation contours', image_copy2)
        image_copy3 = image.copy()
        
        cv2.imwrite(os.path.join(total_image,'simple_'+str(img)+'.jpg'), image_copy3)
        
        img+=1
        
        newImages=[]
        for cnt in contours2:
            idx += 1
            x, y, w, h = cv2.boundingRect(cnt)
            roi = image[y:y + h, x:x + w]
            if h < THIN_THRESHOLD or w < THIN_THRESHOLD:
                continue
            cv2.imwrite(os.path.join(contours_directory,str(idx) + '.png'), roi)
            cv2.rectangle(image, (x, y), (x + w, y + h), (200, 0, 0), 2)
            newImages.append(os.path.join(contours_directory,str(idx) + '.png'))
            
        cv2.imshow('CHAIN_APPROX_SIMPLE Point only', image_copy3)
   #    cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return newImages
        
  