import cv2

from matplotlib import pyplot

img = cv2.imread("../img/ponteiros.png", 0)
cv2.imshow("imagem", img)

pyplot.figure("histograma b")

pyplot.hist(img.ravel(),255,[0,255])

img_equalizada = cv2.equalizeHist(img)
cv2.imshow("imagem equalizada", img_equalizada)
pyplot.hist(img_equalizada.ravel(),255,[0,255])
pyplot.show()