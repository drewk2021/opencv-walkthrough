import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-1", "--image", required = True, help = "input image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)
cv2.waitKey(0)


mask = np.zeros(image.shape[:2], dtype = "uint8")
cX, cY = image.shape[1] // 2, image.shape[0] // 2
cv2.rectangle(mask,(cX - 75, cY - 75),(cX + 75, cY + 75), 255, -1)
cv2.imshow("mask", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("masked", masked)
cv2.waitKey(0)
