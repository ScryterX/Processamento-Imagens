import cv2

img = cv2.imread("../../img/remedio5.jpg")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

metodo = cv2.THRESH_BINARY_INV
limiar, img_bin = cv2.threshold(img_cinza, 190, 255, metodo)


ee = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_dilatada = cv2.dilate(img_bin, ee, iterations=5)
cv2.imshow("imagem dilatada", img_dilatada)

img_erosada=cv2.erode(img_dilatada, ee, iterations=5)
cv2.imshow("imagem erodida", img_erosada)

contornos = cv2.Canny(img_erosada, 0, 100)
cv2.imshow("contornos", contornos)
graos, hierarquia = cv2.findContours(contornos, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

resultado = (len(graos)/2)-1
print(f"A imagem possui {int(resultado)} remédios")

frase = f"A imagem possui {resultado} graos"
texto = cv2.putText(img,frase, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 10, 255))
img_final = cv2.drawContours(img, graos, -1, (255,0,150), 2)

cv2.imshow("resultado", img_final)
cv2.waitKey()