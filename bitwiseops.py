import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required = True,help = "input path to image file")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("original", image)

rectangle = np.zeros((300,300,3), dtype="uint8")
cv2.rectangle(rectangle, (25,25), (275,275), (0,0,255), -1)

# all per-pixel
and1 = cv2.bitwise_and(rectangle, image) # if pixels are both nonzero
cv2.imshow("and",and1)
cv2.waitKey(0)
or1 = cv2.bitwise_or(rectangle, image) # if either pixel is nonzero
xor1 = cv2.bitwise_xor(rectangle,image) # if either but not both pixels is nonzero
NOT1 = cv2.bitwise_not(rectangle, image) # inverts nonzero nature
