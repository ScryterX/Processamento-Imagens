import cv2

img = cv2.imread("../img/chaves3.jpeg")
cv2.imshow("Original", img)

img_menor = cv2.resize(img, None, fx = 0.5, fy = 0.5)
cv2.imshow("nova", img_menor)
cv2.waitKey()