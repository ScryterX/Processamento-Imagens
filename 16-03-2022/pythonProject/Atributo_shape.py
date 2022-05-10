import cv2


img = cv2.imread("img/beira2.png")
altura = img.shape[0]
largura=img.shape[1]
canais=img.shape[2]
print("a imagem possui ", {altura}, " de altura")
print("a imagem possui ", {largura}, " de largura")
print("a imagem possui ", {canais}, " canais")
