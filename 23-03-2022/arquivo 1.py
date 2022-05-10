import cv2
from cv2 import COLOR_BGR2GRAY
from matplotlib import pyplot


img = cv2.imread("../img/folha_color.png")
b,g,r = cv2.split(img)

img_cinza = cv2.cvtColor(img, COLOR_BGR2GRAY)
pyplot.figure("Histograma B")
pyplot.hist(b.ravel(), 255, [0,255])
pyplot.figure("Histograma G")
pyplot.hist(g.ravel(), 255, [0,255])
pyplot.figure("histograma R")
pyplot.hist(r.ravel(), 255, [0,255])
pyplot.show()