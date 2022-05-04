'''
Created on 4 May 2022

@author: maltaweel
'''

from __future__ import print_function

import argparse

from image.plot import Plot

import matplotlib.pyplot as plt
import cv2 as cv

def show_image(img, title):
    if not args.verbose:
        Plot(img, title)
    plt.show()


def parse_arguments():
    """Parses input arguments required to solve puzzle"""
    parser = argparse.ArgumentParser(
        description="A solver for jigsaw puzzles"
    )
    parser.add_argument("--image", type=str, default="out.jpg", help="Input image.")

    parser.add_argument("--size", type=int, help="Single piece size in pixels.")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show best individual after each generation.",
    )
    parser.add_argument(
        "--save", action="store_true", help="Save puzzle result as image."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    image = cv.imread(args.image)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

   
    show_image(image, "Current state")
