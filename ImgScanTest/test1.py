import cv2
import numpy as np

from demo_getRect.utils import point_distance

image = cv2.imread('1.jpg')

# 1、首先转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
srcWidth, srcHeight, channels = image.shape
print(srcWidth, srcHeight)

# 2、之后进行滤波模糊
binary = cv2.medianBlur(gray,91)

# 3、转换为二值图像
ret, after_binary = cv2.threshold(binary, 91, 255, cv2.THRESH_BINARY_INV)

# # 4、边缘检测以及轮廓处理
# third_binary = cv2.Canny(after_binary, 0, 60, apertureSize = 3)

# 5、提取轮廓
_,contours,_ = cv2.findContours(after_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("len(contours)=%d"%(len(contours)))

# cv2.imshow("gray_img", gray)
# cv2.imshow("vague_img", binary)
# cv2.imshow("after_binary_img", after_binary)
# # cv2.imshow("third_binary_img", third_binary)
#
# # 蓝色画出轮廓
# cv2.drawContours(image,contours,-1,(255,0,0),3)
#

test_container=[]
for single_item in contours:
    # 找到最小矩形区域
    rect = cv2.minAreaRect(single_item)

    # 找到最小矩形的顶点
    box = cv2.boxPoints(rect)

    print('this is the type:'+str(type(box)))
    # 取整
    box = np.int0(box)

    if len(box)==4:
        test_container.append(box)

    print("这是点坐标："+str(box))

    # 计算长和宽
    mine_height,mine_length=point_distance(box[0],box[1]),point_distance(box[1],box[2])

    # 原图中卡片的四个角点    绿  红  黑  蓝
    target_img = np.float32([box[1],box[0],box[3],box[2]])
    new_img = np.float32([[0, 0], [0,mine_height], [mine_length, mine_height], [mine_length, 0]])

    # 生成透视变换矩阵
    M = cv2.getPerspectiveTransform(target_img, new_img)
    # 进行透视变换
    dst = cv2.warpPerspective(image, M, (int(mine_length), int(mine_height)))

    cv2.imshow("target_img", dst)

    cv2.drawContours(image, [box], 0, (0, 255, 0), 5)

    # epsilon = 1
    # # 对图像轮廓点进行多边形拟合
    # approx = cv2.approxPolyDP(single_item, epsilon, True)
    #
    # print('这是面积：'+str(cv2.contourArea(approx)))
    # # 如果轮廓为四边形
    # if len(approx)==4:
    #     print(approx)
    # cv2.polylines(image, [approx], True, (0, 255, 0), 2)


# win = cv2.namedWindow('ORG_img', cv2.WINDOW_NORMAL)

cv2.imshow("ORG_img", image)

print("这是记录的矩形")
print(test_container)

# cv2.imshow('test win', img)

# cv2.moveWindow("ORG_img",image,cv2.WINDOW_NORMAL)

cv2.waitKey(0)
cv2.destroyAllWindows()