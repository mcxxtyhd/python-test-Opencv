import cv2 as cv

#灰度模式读取图像
img=cv.imread("img/cz.jpg",0)

#设置阈值进行二值化
th=160
ret,binary1=cv.threshold(img,th,255,cv.THRESH_BINARY_INV)
ret,binary2=cv.threshold(img,th,255,cv.THRESH_BINARY)
ret,binary3=cv.threshold(img,th,255,cv.THRESH_TRUNC)
ret,binary4=cv.threshold(img,th,255,cv.THRESH_TOZERO)
ret,binary5=cv.threshold(img,th,255,cv.THRESH_TOZERO_INV)
ret,binary6=cv.threshold(img,th,255,cv.THRESH_OTSU)
ret,binary7=cv.threshold(img,th,255,cv.THRESH_TRIANGLE)

cv.imshow("THRESH_BINARY_INV",binary1)
# cv.imshow("THRESH_BINARY",binary2)
# cv.imshow("THRESH_TRUNC",binary3)
# cv.imshow("THRESH_TOZERO",binary4)
# cv.imshow("THRESH_TOZERO_INV",binary5)
# cv.imshow("THRESH_OTSU",binary6)
# cv.imshow("THRESH_TRIANGLE",binary7)
cv.waitKey(0)
cv.destroyAllWindows()