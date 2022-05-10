import cv2;

img = cv2.imread("../../img/area_quadrado.bmp")

img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
metodo = cv2.THRESH_BINARY + cv2.THRESH_OTSU
l, img_bin = cv2.threshold(img_cinza, 0, 255, metodo)


contornos, h = cv2.findContours(img_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contornos[0])
img = cv2.drawContours(img, contornos, 0, (0,0,255),2)
cv2.imshow("contornada", img)
cv2.waitKey()