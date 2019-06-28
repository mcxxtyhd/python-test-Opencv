import cv2 as cv
img=cv.imread(r'cz.jpg') #读取图像
cv.imshow("who",img)

if cv.waitKey(1) & 0xFF == ord('e'):
    pass
cv.destroyAllWindows()