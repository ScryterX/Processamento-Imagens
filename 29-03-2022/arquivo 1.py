import cv2

img = cv2.imread("../img/folha_color.png")
cv2.imshow("Original", img)

altura = img.shape[0]
largura = img.shape[1]
centro = (altura / 2, largura/2)
#centro, angulo e escala
matriz = cv2.getRotationMatrix2D(centro, 180, 1)

img_rotacionada = cv2.warpAffine(img, matriz, (largura, altura))
cv2.imshow("Imagem rotacionada", img_rotacionada)
cv2.waitKey()