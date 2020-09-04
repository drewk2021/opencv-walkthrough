import cv2
import argparse
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input file path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)

image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",image)
cv2.waitKey(0)

hist = cv2.calcHist([image],[0],None,[256],[0,256]) # list of images, channels, mask, numBins in list per channel, range of possible pixel values


plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
