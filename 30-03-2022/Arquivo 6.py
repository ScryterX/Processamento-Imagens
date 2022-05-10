import cv2

img = cv2.imread("../img/estacionamento.png")
cv2.imshow("original", img)
img_5x5 = cv2.bilateralFilter(img, 80, 60, 60)
img_tratada = cv2.Laplacian(img_5x5, cv2.CV_8U)
cv2.imshow("bilateral", img_5x5)
cv2.imshow("imagem tratada", img_tratada)

cv2.waitKey()