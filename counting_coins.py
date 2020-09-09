from __future__ import print_function
import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input image path")
args = vars(ap.parse_args())

coins = cv2.imread(args["image"])
graycoins = cv2.cvtColor(coins,cv2.COLOR_BGR2GRAY)
gblur = cv2.GaussianBlur(graycoins,(11,11),0)
cv2.imshow("blurredcoins",gblur)
cv2.waitKey(0)


cannied = cv2.Canny(coins,30,150)
cv2.imshow("Canny", cannied)
cv2.waitKey(0)

(contours, _) = cv2.findContours(cannied.copy(), cv2.RETR_EXTERNAL, cv2
.CHAIN_APPROX_SIMPLE)
print("Counted %d contours in image" % len(contours))

canniedcontours = cannied.copy()
cv2.drawContours(canniedcontours,contours,-1,(0,0,255),3) # image, contours,index, color, thickness
cv2.imshow("contours",canniedcontours)
cv2.waitKey(0)

coinscopy = coins.copy()
cv2.drawContours(coinscopy,contours,0,(0,0,255),3) # image, contours,index, color, thickness
cv2.drawContours(coinscopy,contours,1,(0,0,255),3) # image, contours,index, color, thickness
cv2.drawContours(coinscopy,contours,2,(0,0,255),3) # image, contours,index, color, thickness


for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)
    coin = coins[y:y+h,x:x+w]
    cv2.imshow("Coin",coin)

    mask = np.zeros(coins.shape[:2], dtype="uint8")
    ((centerX,centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask,(int(centerX),int(centerY)),int(radius),255,-1)
    cv2.imshow("masked coin", cv2.bitwise_and(coin,coin,mask=mask))
    cv2.waitKey(0)
