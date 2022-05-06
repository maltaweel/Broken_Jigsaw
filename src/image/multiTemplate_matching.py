'''
Created on 6 May 2022

@author: maltaweel
'''
# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2, os
# construct the argument parser and parse the arguments
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
    help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,
    help="path to the output image")
ap.add_argument("-c", "--crop", type=int, default=0,
    help="whether to crop out largest rectangular region")
args = vars(ap.parse_args())
'''

#the path to the data folder
pn=os.path.abspath(__file__)
pn=pn.split("src")[0]  
contours_directory=os.path.join(pn,'stich')

def templateImageMatching(images):

    # grab the paths to the input images and initialize our images list
    print("[INFO] loading images...")
   
   
    imagePaths = sorted(images)
    imgs = []
    # loop over the image paths, load each one, and add them to our
    # images to stich list
    for imagePath in imagePaths:
        img = cv2.imread(imagePath)
        imgs.append(img)
    # initialize OpenCV's image sticher object and then perform the image
    # stitching
    print("[INFO] stitching images...")
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    # if the status is '0', then OpenCV successfully performed image
    # stitching
    if status == 0:
        # write the output stitched image to disk
        cv2.imwrite(args["output"], stitched)
        # display the output stitched image to our screen
        cv2.imshow("Stitched", stitched)
        cv2.waitKey(0)
    # otherwise the stitching failed, likely due to not enough keypoints)
    # being detected
    else:
        print("[INFO] image stitching failed ({})".format(status))

