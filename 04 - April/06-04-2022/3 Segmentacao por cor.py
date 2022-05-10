import cv2
from funcoes import  limites_hsv
img_original = cv2.imread("../../img/cubo.png")
cv2.imshow("Original", img_original)
img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
lim_inf, lim_sup = limites_hsv(0,255,0)
verde = cv2.inRange(img_hsv, lim_inf, lim_sup)
cv2.imshow("Parte verde", verde)
cv2.waitKey()
