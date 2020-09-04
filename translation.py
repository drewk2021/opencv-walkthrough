import numpy as np
import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required = True, help = "input image file path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("downshift",shifted)
cv2.waitKey(0)
