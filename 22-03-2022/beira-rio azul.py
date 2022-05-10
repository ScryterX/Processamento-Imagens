import cv2

img = cv2.imread("../img/beira3.png")

cv2.imshow("Beira rio", img)
cv2.waitKey(0)

azul =(231,172, 65)
altura = img.shape[0]
largura = img.shape[1]

for i in range(0, altura):
    for j in range(0,largura):
        if img[i][j][2]>240:
            img[i][j]=azul

cv2.imshow("Beira rio 2", img)
cv2.imwrite("../img/beira rio versão activision.png", img)
cv2.waitKey(0)


