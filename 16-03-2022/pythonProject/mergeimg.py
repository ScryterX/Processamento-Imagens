import cv2

r = cv2.imread("img/frutas_R.png", 0)
g = cv2.imread("img/frutas_G.png", 0)
b = cv2.imread("img/frutas_B.png", 0)

img = cv2.merge((b,g,r))

cv2.imshow("Restaurada", img)
cv2.imwrite("img/frutasres.png", img)
cv2.waitKey()