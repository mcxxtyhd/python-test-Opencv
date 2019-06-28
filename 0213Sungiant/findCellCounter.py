
#读取图片
import cv2
import numpy as np

img = cv2.imread('test1.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆结构

# 灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 模糊
medianBlur = cv2.medianBlur(gray,5)

# 二值化
ret, binary = cv2.threshold(medianBlur, 160, 255, cv2.THRESH_BINARY)

#创建白色幕布
white_background = np.ones(binary.shape,np.uint8)*255



# 寻找轮廓
result_findcontours = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE )
#提取轮廓
contours = result_findcontours[1]

for single in contours:
    epsilon = 0.001

    if cv2.contourArea(single)>200:
        # 对图像轮廓点进行多边形拟合
        approx = cv2.approxPolyDP(single, epsilon, True)
        cv2.polylines(white_background, [approx], True, (0, 0, 255), 2)

cv2.imshow('white_background',white_background)

# 腐蚀
erosion = cv2.erode(binary,kernel)

#创建白色幕布
erosion_white_background = np.ones(binary.shape,np.uint8)*255
erosion_result_findcontours = cv2.findContours(erosion,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE )
erosion_contours = erosion_result_findcontours[1]
for single in erosion_contours:
    epsilon = 0.001
    if cv2.contourArea(single)>100:
        # 对图像轮廓点进行多边形拟合
        approx = cv2.approxPolyDP(single, epsilon, True)
        cv2.polylines(erosion_white_background, [approx], True, (0, 0, 255), 3)

# opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)  # 开运算

cv2.imshow('binary',binary)

retval, labels = cv2.connectedComponents(binary)

print('11111111')
print(str(retval),str(len(labels)))
print('11111111')


# cv2.imshow('erosion',erosion)
# cv2.imshow('erosion_white_background',erosion_white_background)

cv2.waitKey(0)
cv2.destroyAllWindows()