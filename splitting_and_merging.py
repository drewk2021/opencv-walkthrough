import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input file path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)

(B, G, R) = cv2.split(image)

cv2.imshow("B",B)
cv2.imshow("merged",cv2.merge([B,G,R]))
cv2.waitKey(0)
