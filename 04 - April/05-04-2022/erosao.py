import cv2
from funcoes import  binariza
img = cv2.imread("../../img/engrenagem.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", img)

img_binaria = binariza(img_cinza, 80)
cv2.imshow("nova", img_binaria)

ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_dilatada=cv2.erode(img_binaria, ee, iterations=2)
cv2.imshow("erosão", img_dilatada)
cv2.waitKey()