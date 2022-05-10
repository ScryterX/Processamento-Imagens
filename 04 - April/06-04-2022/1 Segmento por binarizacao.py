import cv2
from funcoes import  binariza
img = cv2.imread("../../img/cafe.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", img)
cv2.imshow("Escala de cinza", img_cinza)

limiar, img_bin = cv2.threshold(img_cinza, 185, 255, cv2.THRESH_TOZERO)
print(limiar)
cv2.imshow("img_bin", img_bin)
cv2.waitKey()