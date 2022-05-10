import cv2
from funcoes import  binariza
img = cv2.imread("../../img/cafe.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", img)
cv2.imshow("Escala de cinza", img_cinza)
metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU

limiar, img_bin = cv2.threshold(img_cinza, 0, 255, metodo)
print(limiar)
cv2.imshow("img_bin", img_bin)
cv2.waitKey()