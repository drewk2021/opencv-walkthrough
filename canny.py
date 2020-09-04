import cv2
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gblur = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("gaussianblurredgreyscale",gblur)
cv2.waitKey(0)

cannied = cv2.Canny(image, 30, 150)
cv2.imshow("cannyedges",cannied)
cv2.waitKey(0)
