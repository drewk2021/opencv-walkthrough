import numpy as np
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required = True, help = "please input path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)


rotated = imutils.rotate(image, -45)
cv2.imshow("Rotated45",rotated)
cv2.waitKey(0)
