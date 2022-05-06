'''
Created on 6 May 2022

@author: maltaweel
'''
# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
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


def templateImageMatching(images):

    # grab the paths to the input images and initialize our images list
    print("[INFO] loading images...")
   
    # initialize OpenCV's image sticher object and then perform the image
    # stitching
    print("[INFO] stitching images...")
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)


