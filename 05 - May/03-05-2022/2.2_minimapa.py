import cv2;
from cv2 import FONT_HERSHEY_SIMPLEX

from funcoes import limites_hsv

img_original = cv2.imread("../../img/islandia.png")

#área dedicada a encontrar a montanha com neve
img_cinza = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
metodo = cv2.THRESH_BINARY + cv2.THRESH_OTSU
l, img_bin = cv2.threshold(img_cinza, 0, 255, metodo)
cv2.imshow("bin", img_bin)

ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_dilatada = cv2.dilate(img_bin, ee, iterations=2)
img_erodida=cv2.erode(img_dilatada, ee, iterations=8)
img_dilatada = cv2.dilate(img_erodida, ee, iterations=10)
cv2.imshow("bin", img_dilatada)
contornos, h = cv2.findContours(img_dilatada, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contornos[0])
img = cv2.drawContours(img_original, contornos, -1, (190,0,255),2)
cv2.imshow("contornada", img)
area=0.0
for gelo in contornos:
    area += cv2.contourArea(gelo)
print(area)

cv2.imshow("contornada", img)

#área dedicada a encontrar a ilha
img_5x5 = cv2.bilateralFilter(img_original, 10,35, 35)
img_hsv = cv2.cvtColor(img_5x5, cv2.COLOR_BGR2HSV)
lim_inf, lim_sup = limites_hsv(154,96,74)
azul = cv2.inRange(img_hsv, lim_inf, lim_sup)

metodo = cv2.THRESH_BINARY_INV
l, img_inv = cv2.threshold(azul, 0, 255, metodo)
img_dilatada = cv2.dilate(img_inv, ee, iterations=2)
img_erodida=cv2.erode(img_dilatada, ee, iterations=4)
contornos, h = cv2.findContours(img_erodida, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contornos[0])
img = cv2.drawContours(img_original, contornos, 0, (0,0,255),2)
cv2.imshow("contornada", img)


cv2.waitKey()