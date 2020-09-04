import numpy as np
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required = True,help = "input path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

resized = imutils.resize(image, height = 100)
cv2.imshow("resized",resized)
cv2.waitKey(0)
