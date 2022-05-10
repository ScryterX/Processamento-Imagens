import cv2
from cv2 import COLOR_BGR2GRAY

img = cv2.imread("img/frutas.png")
cv2.imshow("frutas", img)

img_cinza = cv2.cvtColor(img, COLOR_BGR2GRAY)
cv2.imshow("imagem cinza",img_cinza)
cv2.waitKey()