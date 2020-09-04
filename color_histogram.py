import cv2
import argparse
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

channels = cv2.split(image)
colors = ["b","g","r"]

plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")

for (channel,color) in zip(channels,colors):
    hist = cv2.calcHist([channel],[0],None,[256],[0,256])
    plt.plot(hist,color = color)
    plt.xlim([0,256])


plt.show()

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[0],channels[1]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation="nearest")
ax.set_title("Blue and Green 2D Histogram")
plt.colorbar(p)
plt.show()
cv2.waitKey(0)
