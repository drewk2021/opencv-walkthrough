import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-1","--image",required=True,help="input image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

differentBlurs = np.hstack([cv2.blur(image,(3,3)),cv2.blur(image,(5,5)),cv2.blur(image,(7,7))])
cv2.imshow("blurs",differentBlurs)
cv2.waitKey(0)

gaussianBlurs = np.hstack([cv2.GaussianBlur(image,(3,3),0),cv2.GaussianBlur(image,(5,5),0),cv2.GaussianBlur(image,(7,7),0)]) # weighted based on proximity to center
cv2.imshow("gaussian",gaussianBlurs)
cv2.waitKey(0)

medianBlurs = np.hstack([cv2.medianBlur(image,3),cv2.medianBlur(image,5),cv2.medianBlur(image,7)])
cv2.imshow("median",medianBlurs)
cv2.waitKey(0)

bilateralBlurs = np.hstack([cv2.bilateralFilter(image,5,21,21),cv2.bilateralFilter(image,7,31,31),cv2.bilateralFilter(image,9,41,41)])
cv2.imshow("bilateral",bilateralBlurs)
cv2.waitKey(0)
