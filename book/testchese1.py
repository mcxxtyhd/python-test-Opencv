# -- coding: utf-8 --
import cv2
import cv2
import numpy as np
from scipy import ndimage

#这个是滤波器使用的模板矩阵
kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])

# #自定义卷积核
# kernel_sharpen_1 = np.array([
#         [-1,-1,-1],
#         [-1,9,-1],
#         [-1,-1,-1]])
# kernel_sharpen_2 = np.array([
#         [1,1,1],
#         [1,-7,1],
#         [1,1,1]])
# kernel_sharpen_3 = np.array([
#         [-1,-1,-1,-1,-1],
#         [-1,2,2,2,-1],
#         [-1,2,8,2,-1],
#         [-1,2,2,2,-1],
#         [-1,-1,-1,-1,-1]])/8.0
# #卷积
# output_1 = cv2.filter2D(image,-1,kernel_sharpen_1)
# output_2 = cv2.filter2D(image,-1,kernel_sharpen_2)
# output_3 = cv2.filter2D(image,-1,kernel_sharpen_3)

img_path="cheese.jpg"
# img_path="theoimg.jpg"
org_img=cv2.imread(img_path)


#以灰度的方式加载图片
img = cv2.imread(img_path, 0)
# cv2.imshow("gray_img", img)

#通过使用模板矩阵进行高通滤波
k3 = ndimage.convolve(img, kernel_3x3)
# cv2.imshow("3x3", k3)
k5 = ndimage.convolve(img, kernel_5x5)

#使用OpenCV 模糊滤波函数
blurred = cv2.GaussianBlur(img, (11, 11), 0)
cv2.imshow("blurred", blurred)

# cv2.imshow("5x5", k5)

g_hpf = img - blurred
# 灰度图-高通滤波
g_hpf = img - blurred
cv2.imshow("g_hpf", g_hpf)

blur_g_hpf=cv2.medianBlur(g_hpf,3)
cv2.imshow("blur_g_hpf",blur_g_hpf)

# circles = cv2.HoughCircles(g_hpf, cv2.HOUGH_GRADIENT, 1, 127, param1=100, param2 = 30, minRadius = 0,  maxRadius = 0)
# circles = np.uint16(np.around(circles))
#
# for i in circles[0,:]:
#     # 画圈
#     # draw the outer circle
#     cv2.circle(org_img, (i[0], i[1]), i[2],(0, 255, 0),2)
#
#     # 画中心点
#     # draw the center of the circle
#     cv2.circle(org_img, (i[0], i[1]), 2, (255, 0,0), 3)

#显示原始图像
cv2.imshow("org", org_img)
cv2.waitKey()
cv2.destroyAllWindows()
