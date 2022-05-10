import cv2

img_maior = cv2.imread("../img/praia_invertida.png")
img = cv2.resize(img_maior, None, fx = 0.3, fy = 0.3)
cv2.imshow("Original", img)

altura = img.shape[0]
largura = img.shape[1]
centro = (largura / 2, altura/2)
#centro, angulo e escala
matriz = cv2.getRotationMatrix2D(centro, 180, 1)

img_rotacionada = cv2.warpAffine(img, matriz, (largura, altura))
cv2.imshow("Imagem redimensionada e reinvertida", img_rotacionada)
cv2.waitKey()