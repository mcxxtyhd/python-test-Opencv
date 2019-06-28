import numpy as np
import cv2

#读取图片
img = cv2.imread('test1.jpg')

# 1、首先转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
srcWidth, srcHeight, channels = img.shape
print(srcWidth, srcHeight)

# 2、之后进行滤波模糊
binary = cv2.medianBlur(gray,3)

# 3、转换为二值图像
ret, after_binary = cv2.threshold(binary, 190, 255, cv2.THRESH_BINARY)

# 4、边缘检测以及轮廓处理
third_binary = cv2.Canny(after_binary, 0, 60, apertureSize = 3)

#二值化，canny检测
binaryImg = cv2.Canny(img,50,200)

#寻找轮廓
#也可以这么写：
# binary,h, hierarchy = cv2.findContours(third_binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#这样，可以直接用contours表示
h = cv2.findContours(third_binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE )

print('here is the items nums :'+str(len(h)))
# for itemTheo in h:

#提取轮廓
contours = h[1]

print('here is he type'+str(type(contours)))
#查看轮廓数量
print (len(contours))

#创建白色幕布
temp = np.ones(third_binary.shape,np.uint8)*255

#创建白色幕布
temp1 = np.ones(third_binary.shape,np.uint8)*255
# #画出轮廓：temp是白色幕布，contours是轮廓，-1表示全画，然后是颜色，厚度
cv2.drawContours(temp1,contours,-1,(0,255,0),3)
cv2.imshow('drawContours',temp1)

for singleitem in contours:
    # epsilon = 0.00001 * cv2.arcLength(cnt,True)
    epsilon = 0.001

    # 对图像轮廓点进行多边形拟合
    approx = cv2.approxPolyDP(singleitem, epsilon, True)
    print('approx length:'+str(len(approx)))
    # cv2.drawContours(img, approx, -1, (0, 0, 255), 3)

    cv2.polylines(temp, [approx], True, (0, 0, 255), 2)

cv2.imshow('contours',temp)

cv2.waitKey(0)
cv2.destroyAllWindows()
