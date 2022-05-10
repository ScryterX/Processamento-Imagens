import cv2

img_frutas = cv2.imread("../img/frutas.png")
cv2.imshow("Original", img_frutas)

img_vint = cv2.add(img_frutas, -70)
cv2.imshow("vintage", img_vint)
img_future = cv2.add(img_frutas, 120)
cv2.imshow("future", img_future)
cv2.waitKey()