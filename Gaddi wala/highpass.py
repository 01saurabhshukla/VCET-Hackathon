import cv2
import numpy as np

img = cv2.imread("image.jpg")
image = cv2.resize(img, (400, 300))
gaussian_blur = cv2.GaussianBlur(image, (7,7), 2)

sharpend1 = cv2.addWeighted(image, 1.5, gaussian_blur, -0.5, 0)
sharpend2 = cv2.addWeighted(image, 3.5, gaussian_blur, -2.5, 0)
sharpend3 = cv2.addWeighted(image, 7.5, gaussian_blur, -6.5, 0)

cv2.imshow("sharpend1", sharpend1)
cv2.imshow("sharpend3", sharpend3)
cv2.imshow("sharpend2", sharpend2)
cv2.imshow("original", image)
cv2.waitKey(0)