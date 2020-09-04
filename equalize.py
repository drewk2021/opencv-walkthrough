import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization",np.hstack([image,equalized]))
cv2.waitKey(0)
