import cv2
from cv2 import waitKey, CascadeClassifier, rectangle, COLOR_BGR2GRAY
captura = cv2.VideoCapture("D:\Homem-Aranha.mkv")
# captura = cv2.VideoCapture(0)
# i = 0

har_carregado = CascadeClassifier("../10-05-2022/haarcascades/haarcascade_frontalface_default.xml")
eyes_pattern = CascadeClassifier("../10-05-2022/haarcascades/haarcascade_eye.xml")
while True:
    status, img = captura.read()
    img = cv2.resize(img,None, fx=0.5, fy=0.5)


    img_cinza = cv2.cvtColor(img, COLOR_BGR2GRAY)
    rostos = har_carregado.detectMultiScale(img_cinza, scaleFactor=2)
    olhos = eyes_pattern.detectMultiScale(img_cinza, scaleFactor=2.5)
    for (x, y, l, a) in rostos:
        rectangle(img, (x, y), (x + l, y + a), (25, 255, 20), 2)
    for (x, y, l, a) in olhos:
        rectangle(img, (x, y), (x + l, y + a), (255, 0, 220), 2)
    cv2.imshow("frame", img)
    # cv2.imwrite(f"apagar/img{i}.jpg", captura)
    # i+=1
    if (waitKey(1) == 27):
        break