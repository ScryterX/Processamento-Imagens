import cv2
from cv2 import COLOR_BGR2GRAY
from matplotlib import pyplot
img = cv2.imread("../img/folha_color.png")
img_cinza = cv2.cvtColor(img, COLOR_BGR2GRAY)
altura = img.shape[0]
largura = img.shape[1]

for i in range(0, altura):
    for j in range(0,largura):
        if img_cinza[i][j]>170:
            img_cinza[i][j]=255
        else:
            img_cinza[i][j]=0

cv2.imshow("Preto e branco", img_cinza)
cv2.imwrite("../img/folha_color em 2 canais.png", img_cinza)
cv2.waitKey(0)