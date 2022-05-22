import cv2
#from cv2 import *
from cv2 import COLOR_BGR2GRAY, CascadeClassifier, rectangle

har_carregado = CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eyes_pattern = CascadeClassifier("haarcascades/haarcascade_eye.xml")
img = cv2.imread("fotos/img3.jpeg")
img = cv2.resize(img, None, fx=0.5, fy = 0.5)
img_cinza = cv2.cvtColor(img, COLOR_BGR2GRAY)

rostos = har_carregado.detectMultiScale(img_cinza, scaleFactor=2)
olhos=eyes_pattern.detectMultiScale(img_cinza, scaleFactor=2.5)
print(rostos)
print(olhos)
for (x,y,l,a) in rostos:
    rectangle(img, (x,y), (x+l, y+a), (25,255,20),2)
for (x,y,l,a) in olhos:
    rectangle(img, (x,y), (x+l, y+a), (255,0,220),2)

cv2.imshow("faces", img)
cv2.waitKey()
