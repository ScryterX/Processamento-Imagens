import cv2

img = cv2.imread("../img/radiografia.png",0)
cv2.imshow("Original 1", img)
img_suave = cv2.bilateralFilter(img, 10,35, 35)
img_detalhes = cv2.subtract(img, img_suave)
img_detalhes = 3*img_detalhes
img_resultado = cv2.add(img, img_detalhes)

cv2.imshow("Suavizada 2", img_suave)
cv2.imshow("detalhes  3", img_detalhes)
cv2.imshow("resultado 4", img_resultado)
cv2.waitKey()