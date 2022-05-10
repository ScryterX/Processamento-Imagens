import cv2
from matplotlib import numpy

def binariza (img, limiar, obj = True):
    linhas = img.shape[0]
    colunas = img.shape[1]

    for i in range (0, linhas):
        for j in range (0, colunas):
            if obj == False:
                if (img[i][j]) < limiar:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
            else:
                if(img[i][j]) > limiar:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
    return img


def limites_hsv(b,g,r):
    bgr_color = numpy.uint8([[[b,g,r]]])
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
    h_inf = hsv_color[0][0][0] - 20
    h_sup = hsv_color[0][0][0] + 20
    if h_inf < 0:
        h_inf = 0
    if h_sup > 255:
        h_sup = 255
    hsv_inferior = numpy.array([[[h_inf, 75, 75]]])
    hsv_superior = numpy.array([[[h_sup, 255, 255]]])
    return hsv_inferior, hsv_superior