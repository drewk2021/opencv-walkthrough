import numpy as np
import cv2

canvas = np.zeros((300,300,3),dtype="uint8")

green = (0,255,0)
cv2.line(canvas,(100,100),(300,300),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)


# re-initialize black canvas
canvas = np.zeros((300,300,3),dtype="uint8")
centerX, centerY = canvas.shape[1] // 2, canvas.shape[0] // 2

cv2.circle(canvas,(centerX,centerY),46,green,-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
