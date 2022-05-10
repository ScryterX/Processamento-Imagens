import cv2
from funcoes import limites_hsv

img = cv2.imread("../../img/remedio5.jpg")
cv2.imshow("original",img)
img_5x5 = cv2.bilateralFilter(img, 80, 60, 60)
img_tratada = cv2.Laplacian(img, cv2.CV_8U)
cv2.imshow("bilateral", img_5x5)
cv2.imshow("imagem tratada", img_tratada)
ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
img_retratada = cv2.dilate(img_tratada, ee, iterations=16)
metodo = cv2.THRESH_BINARY_INV
limiar, img_bin = cv2.threshold(img_retratada, 190, 255, metodo)
ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
contornos = cv2.Canny(img_bin, 70, 100)
cv2.imshow("contornos", contornos)

#img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU

#limiar, img_bin = cv2.threshold(img_cinza, 0, 255, metodo)



#ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#img_dilatada = cv2.dilate(img_bin, ee, iterations=2)
#img_erosada=cv2.erode(img_dilatada, ee, iterations=3)

#contornos = cv2.Canny(img_erosada, 70, 100)

#graos, hierarquia = cv2.findContours(contornos, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#print(f"A imagem possui {len(graos)} grãos")

#frase = f"A imagem possui {len(graos)} graos"
#texto = cv2.putText(img,frase, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 10, 255))
#img_final = cv2.drawContours(img, graos,-1, (255,0,150), 2)
#cv2.imshow("resultado", img_final)
cv2.waitKey()