import cv2

img = cv2.imread("../img/estacionamento.png")
cv2.imshow("original", img)
img_5x5 = cv2.bilateralFilter(img, 70,58, 58)

cv2.imshow("5x5", img_5x5)

cv2.waitKey()