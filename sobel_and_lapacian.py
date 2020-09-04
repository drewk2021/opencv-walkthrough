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
