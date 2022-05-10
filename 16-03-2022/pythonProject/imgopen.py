import cv2
img = cv2.imread("img/frutas.png")

cv2.imshow("frutas", img)

b, g, r = cv2.split(img)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)

cv2.imwrite("img/frutas_R.png", r)
cv2.imwrite("img/frutas_G.png", g)
cv2.imwrite("img/frutas_B.png", b)
cv2.waitKey()
