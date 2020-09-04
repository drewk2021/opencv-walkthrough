from __future__ import print_function
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required = True, help = "Path to image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
print("width : %d pixels" % image.shape[1]) #columns
print("height : %d pixels" % image.shape[0]) #rows
print("channels : %d" % image.shape[2])

cv2.imshow("America", image)
cv2.waitKey(0)

cv2.imwrite("Images\\baldeagle.png",image)
