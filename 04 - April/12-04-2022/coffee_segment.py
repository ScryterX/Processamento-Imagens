import cv2
from funcoes import limites_hsv

img = cv2.imread("../../img/cafe.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
limiar, img_bin = cv2.threshold(img_cinza, 0, 255, metodo)



ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
img_dilatada = cv2.dilate(img_bin, ee, iterations=2)
img_erosada=cv2.erode(img_dilatada, ee, iterations=3)

contornos = cv2.Canny(img_erosada, 70, 100)

graos, hierarquia = cv2.findContours(contornos, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"A imagem possui {len(graos)} grãos")

frase = f"A imagem possui {len(graos)} graos"
texto = cv2.putText(img,frase, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 10, 255))
img_final = cv2.drawContours(img, graos,-1, (255,0,150), 2)
cv2.imshow("resultado", img_final)
cv2.waitKey()