from matplotlib import pyplot as plt
import cv2
import numpy as np
import argparse


def plot_histogram(image, title, mask = None):
    channels = cv2.split(image)
    colors = ('b','g','r')
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (channel, color) in zip(channels,colors):
        hist = cv2.calcHist([channel],[0],mask,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])

ap = argparse.ArgumentParser()
ap.add_argument("-1", "--image", required = True, help = "input image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
plot_histogram(image,"original")

mask = np.zeros(image.shape[:2],dtype="uint8")
cv2.rectangle(image,(15,15),(130,100),255,-1)

masked = cv2.bitwise_and(image,image,mask=mask)
plot_histogram(image,"masked",mask)
plt.show()
cv2.waitKey(0)
