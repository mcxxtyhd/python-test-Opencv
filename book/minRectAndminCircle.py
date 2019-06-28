import cv2

import numpy as np

img =cv2.imread('theoimg.jpg',cv2.IMREAD_UNCHANGED)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)
#先将图像转化成灰度，再转化成二值图像

cv2.imshow('thresh',thresh)
image,contours,hier=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#检测边缘

print(str(len(contours)))

for c in contours:
    # print(str(type(c)))

    x,y,w,h = cv2.boundingRect(c)
    #用一个最小的矩形，把找到的形状包起来,还有一个带旋转的矩形
    #返回(x,y)为矩形左上角坐标，w,h分别是宽和高

    # 绿色
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)#确定对角线然后画出矩阵

    rect = cv2.minAreaRect(c)#找到最小矩形区域

    box = cv2.boxPoints(rect)#找到最小矩形的顶点
    print(str(box))
    # 取整
    box = np.int0(box)
    cv2.drawContours(img,[box],0,(0,0,255),5)

    (x,y),radius = cv2.minEnclosingCircle(c)#找到最小圆，并返回圆心坐标和半径

    center=(int(x),int(y))
    radius = int(radius)

    # 红色画最小的圆
    img = cv2.circle(img,center,radius,(0,0,255),2)

# 蓝色画出轮廓
cv2.drawContours(img,contours,-1,(255,0,0),1)
cv2.imshow('contours',img)
cv2.waitKey()
