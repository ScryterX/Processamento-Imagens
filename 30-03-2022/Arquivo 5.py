import cv2

img = cv2.imread("../img/goku_vegeta.png",0)
cv2.imshow("original", img)
img_5x5 = cv2.Laplacian(img, cv2.CV_8U)

cv2.imshow("5x5", img_5x5)

cv2.waitKey()