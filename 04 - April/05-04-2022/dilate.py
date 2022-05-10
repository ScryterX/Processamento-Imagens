import cv2
from funcoes import  binariza
img_original = cv2.imread("../../img/ovos.jpeg")
img = cv2.resize(img_original, None, fx = 0.3, fy = 0.3 )
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img_cinza)
img_binaria = binariza(img_cinza, 145)
cv2.imshow("binarizada", img_binaria)

ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_erodida=cv2.erode(img_binaria, ee, iterations=2)
cv2.imshow("erosao", img_erodida)

img_dilatada = cv2.dilate(img_erodida, ee, iterations=2)
cv2.imshow("dilatada", img_dilatada)
cv2.waitKey()