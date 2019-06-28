import cv2
import numpy as np

img = cv2.imread('img/road.jpg')
# 灰度处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 2、之后进行滤波模糊
binary = cv2.medianBlur(gray, 5)

# 3、转换为二值图像
ret, after_binary = cv2.threshold(binary, 180, 255, cv2.THRESH_BINARY_INV)

# canny边缘处理
edges = cv2.Canny(gray,250,255)
line = 300
minLineLength = 20
# HoughLinesP函数是概率直线检测，注意区分HoughLines函数
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, lines=line, minLineLength=minLineLength)
# 降维处理
lines1 = lines[:,0,:]
# line 函数勾画直线
# (x1,y1),(x2,y2)坐标位置
# (0,255,0)设置BGR通道颜色
# 2 是设置颜色粗浅度
for x1,y1,x2,y2 in lines1:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)

# 显示图像
cv2.imshow("edges", edges)
cv2.imshow("after_binary", after_binary)
cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
