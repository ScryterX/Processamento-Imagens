import cv2
from funcoes import  binariza
img = cv2.imread("../../img/folha_color.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img_cinza)
img_binaria = binariza(img_cinza, 175, False)
cv2.imshow("nova", img_binaria)

ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_erodida=cv2.erode(img_binaria, ee, iterations=1)
cv2.imshow("erosao", img_erodida)
cv2.waitKey()
