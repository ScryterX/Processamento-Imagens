import cv2;

from funcoes import limites_hsv

img_original = cv2.imread("../../img/islandia.png")
#cv2.imshow("Original", img_original)

img_5x5 = cv2.bilateralFilter(img_original, 10,35, 35)
#cv2.imshow("5x5", img_5x5)

img_hsv = cv2.cvtColor(img_5x5, cv2.COLOR_BGR2HSV)
lim_inf, lim_sup = limites_hsv(154,96,74)
azul = cv2.inRange(img_hsv, lim_inf, lim_sup)

metodo = cv2.THRESH_BINARY_INV
l, img_inv = cv2.threshold(azul, 0, 255, metodo)

ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_dilatada = cv2.dilate(img_inv, ee, iterations=2)
#cv2.imshow("dilatada", img_dilatada)

img_erodida=cv2.erode(img_dilatada, ee, iterations=4)
#cv2.imshow("erosao", img_erodida)

contornos, h = cv2.findContours(img_erodida, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contornos[0])
img = cv2.drawContours(img_original, contornos, 0, (0,0,255),2)
cv2.imshow("contornada", img)




# img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# metodo = cv2.THRESH_BINARY + cv2.THRESH_OTSU
# l, img_bin = cv2.threshold(img_cinza, 0, 255, metodo)
#
#
# contornos, h = cv2.findContours(img_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# area = cv2.contourArea(contornos[0])
# img = cv2.drawContours(img, contornos, 0, (0,0,255),2)
# cv2.imshow("contornada", img)
cv2.waitKey()