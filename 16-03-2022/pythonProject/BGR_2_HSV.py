import cv2
from cv2 import *
from cv2 import COLOR_BGR2HSV

img = cv2.imread("img/chaves1.jpeg")

img_hsv = cv2.cvtColor(img, COLOR_BGR2HSV)

H,S,V = cv2.split(img_hsv)

cv2.imshow("Canal Hue", H)
cv2.imshow("Canal Saturation", S)
cv2.imshow("Canal Value", V)
cv2.waitKey()