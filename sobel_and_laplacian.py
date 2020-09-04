import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",image)

laplacian = cv2.Laplacian(image,cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv2.imshow("lap",laplacian)
cv2.waitKey(0)

sobelX = cv2.Sobel(image,cv2.CV_64F,1,0) # derivative in x, finds vertical edge-like regions
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1) # derivative in y, finds horizontal edge-like regions

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("sobelx",sobelX)
cv2.imshow("sobely",sobelY)
cv2.imshow("sobelcombined",sobelCombined)
cv2.waitKey(0)
