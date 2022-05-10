import cv2

img_mesa = cv2.imread("../img/mesa.png")
cv2.imshow("Original", img_mesa)

img_ficha = cv2.imread("../img/ficha2.png")
cv2.imshow("Original", img_ficha)

img_novo = cv2.subtract(img_ficha, img_mesa)
cv2.imshow("aaa", img_novo)
cv2.waitKey()