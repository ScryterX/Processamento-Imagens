import cv2
img = cv2.imread("img/goku_vegeta.png")

b, g, r = cv2.split(img)

cv2.imshow("red", r)
cv2.imshow("green", g)
cv2.imshow("blue", b)

cv2.imwrite("img/goku_vegeta_R.png", r)
cv2.imwrite("img/goku_vegeta_G.png", g)
cv2.imwrite("img/goku_vegeta_B.png", b)
cv2.waitKey()