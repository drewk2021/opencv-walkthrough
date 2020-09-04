from __future__ import print_function
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required = True ,help = "Please supply image file")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)

image[0:100, 0:100] = (255,0,0)

cv2.imshow("Updated",image)
cv2.waitKey(0)
