import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="path to image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

flipped = cv2.flip(image,1) # 1 is horizontal, 0 is vertical, -1 is both.
cv2.imshow("flipped",flipped)
cv2.waitKey(0)
