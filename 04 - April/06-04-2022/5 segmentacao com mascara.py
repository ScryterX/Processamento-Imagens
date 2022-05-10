import cv2
from funcoes import  limites_hsv
img_original = cv2.imread("../../img/cubo.png")
cv2.imshow("Original", img_original)
img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

lim_inf_r, lim_sup_r = limites_hsv(25,10,255)
lim_inf_yellow, lim_sup_yellow = limites_hsv(25,10,255)

vermelho = cv2.inRange(img_hsv, lim_inf_r, lim_sup_r)
amarelo = cv2.inRange(img_hsv, lim_inf_yellow, lim_inf_yellow)
cv2.imshow("amarelo", amarelo)
ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print(lim_inf_yellow)
print(lim_sup_yellow)
vermelho = cv2.erode(vermelho, ee)

mascara=vermelho+amarelo
result = cv2.bitwise_and(img_original, img_original, mask=vermelho)

cv2.imshow("Parte verde", result)
cv2.waitKey()
