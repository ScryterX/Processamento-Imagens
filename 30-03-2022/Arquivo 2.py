import cv2

img = cv2.imread("../img/lenna.png")
cv2.imshow("original", img)
img_5x5 = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("5x5", img_5x5)

cv2.waitKey()