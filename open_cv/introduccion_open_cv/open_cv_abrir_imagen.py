import cv2 as cv

img = cv.imread('seccion_2/img/Cat2.jpg')
img = cv.resize(img, (800, 600))


cv.imshow('cat', img)
cv.waitKey(0)