import cv2

img = cv2.imread("../img/lenna.png")
cv2.imshow("original", img)
img_5x5 = cv2.bilateralFilter(img, 10,35, 35)

cv2.imshow("5x5", img_5x5)

cv2.waitKey()