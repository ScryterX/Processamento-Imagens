import cv2

r = cv2.imread("img/goku_vegeta_R.png", 0)
g = cv2.imread("img/goku_vegeta_G.png", 0)
b = cv2.imread("img/goku_vegeta_B.png", 0)

img = cv2.merge((b,g,r))

cv2.imshow("Restore", img)
cv2.imwrite("img/Restore.png", img)
cv2.waitKey()