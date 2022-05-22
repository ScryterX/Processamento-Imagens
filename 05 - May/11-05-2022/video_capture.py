import cv2
from cv2 import waitKey


captura = cv2.VideoCapture(0)
# i = 0


while True:
    status, img = captura.read()
    cv2.imshow("frame", img)
    # cv2.imwrite(f"apagar/img{i}.jpg", captura)
    # i+=1
    if (waitKey(1) == 27):
        break