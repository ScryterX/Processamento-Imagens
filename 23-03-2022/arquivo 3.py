import cv2
from matplotlib import pyplot


img1 = cv2.imread("../img/chaves1.jpeg")
img2 = cv2.imread("../img/chaves2.jpeg")
cv2.imshow("chaves1",img1)
cv2.imshow("chaves2",img2)
pyplot.figure("Histograma Chaves 1 e 3")
pyplot.hist(img1.ravel(), 255, [0,255])
pyplot.hist(img2.ravel(), 255, [0,255])
pyplot.show()

