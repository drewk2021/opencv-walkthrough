import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required = True,help = "input path to image file")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("original", image)


M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image,M) # cv2 adds with min/max of 0/255. Clipped.
cv2.imshow("added",added)
cv2.waitKey(0)
