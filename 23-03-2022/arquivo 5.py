import cv2
from cv2 import *
from cv2 import COLOR_BGR2HSV, COLOR_HSV2BGR

img = cv2.imread("../img/chaves3.jpeg")                     #carrega imagem
cv2.imshow("Chaves 3 - Original", img)                      #abre a imagem
img_hsv = cv2.cvtColor(img, COLOR_BGR2HSV)                  #converte imagem RGB para HSV

H,S,V = cv2.split(img_hsv)                                  #separa imagem HSV em seus canais

img_equalizada = cv2.equalizeHist(V)                        #equaliza canal V

img = cv2.merge((H,S,img_equalizada))                       #junta imagem HSV em seus canais

img_bgr = cv2.cvtColor(img, COLOR_HSV2BGR)                  #converte imagem HSV em RGB
cv2.imshow("Chaves 3 - Remaster", img_bgr)                  #abre imagem refeita
cv2.imwrite("../img/chaves3_equaliz.jpeg", img_bgr)         #salva imagem
cv2.waitKey()