# -- coding: utf-8 --
import cv2
import cv2
import numpy as np
from scipy import ndimage

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])

img_path="cheese.jpg"

img=cv2.imread(img_path)

# 1、先变灰
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#显示灰度图像
cv2.imshow("gray_img", gray_img)

# # 2、再模糊
# blur_img=cv2.medianBlur(gray_img,9)
# #显示模糊图像
# cv2.imshow("blur_img", blur_img)

# # 2、二值化
ret,binary_img=cv2.threshold(gray_img,20,255,cv2.THRESH_BINARY_INV)
# #显示图像
cv2.imshow("binary_img", binary_img)


# canny查找边缘
canny_img=cv2.Canny(binary_img,50,150)
# #显示图像
cv2.imshow("canny_img", canny_img)

# # 再模糊
# blur_img=cv2.medianBlur(binary_img,3)
# #显示模糊图像
# cv2.imshow("blur_img", blur_img)

# circles = cv2.HoughCircles(binary_img, cv2.HOUGH_GRADIENT, 1, 127, param1=100, param2 = 30, minRadius = 0,  maxRadius = 0)
# circles = np.uint16(np.around(circles))
#
# for i in circles[0,:]:
#     # 画圈
#     # draw the outer circle
#     cv2.circle(img, (i[0], i[1]), i[2],(0, 255, 0),2)
#
#     print('这是半径：'+str(i[2]))
#
#     # 画中心点
#     # draw the center of the circle
#     cv2.circle(img, (i[0], i[1]), 2, (255, 0,0), 3)


# #以灰度的方式加载图片
# img = cv2.imread(img_path, 0)
# # cv2.imshow("gray_img", img)
#
# k5 = ndimage.convolve(img, kernel_5x5)
#
# #使用OpenCV 模糊滤波函数
# blurred = cv2.GaussianBlur(img, (11, 11), 0)
# cv2.imshow("blurred", blurred)
#
# cv2.imshow("5x5", k5)
#
# g_hpf = img - blurred
# # 灰度图-高通滤波
# g_hpf = img - blurred
# cv2.imshow("g_hpf", g_hpf)

# cv2.imshow("HoughCircles", img)
cv2.waitKey()
cv2.destroyAllWindows()
