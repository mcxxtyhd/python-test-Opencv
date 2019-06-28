import math
import numpy as np
import cv2

from demo_getRect.utils import order_array, point_distance

image = cv2.imread('targetImg.jpg')

# 1、首先转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
srcWidth, srcHeight, channels = image.shape
print(srcWidth, srcHeight)

# 2、之后进行滤波模糊
binary = cv2.medianBlur(gray,3)

# 3、转换为二值图像
ret, after_binary = cv2.threshold(binary, 80, 255, cv2.THRESH_BINARY)

# 4、边缘检测以及轮廓处理
third_binary = cv2.Canny(after_binary, 0, 60, apertureSize = 3)

# 5、提取轮廓后，拟合外接多边形（矩形）
_,contours,_ = cv2.findContours(third_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("len(contours)=%d"%(len(contours)))

# # 6、提取面积最大的轮廓并用多边形将轮廓包围
# for idx,c in enumerate(contours):
#
#     # 这是精度
#     epsilon = 0.00001
#     while True:
#         approx = cv2.approxPolyDP(c,epsilon,True)
#         print("idx,epsilon,len(approx),len(c)=%d,%d,%d,%d"%(idx,epsilon,len(approx),len(c)))
#
#         # 少于4个点
#         if (len(approx) < 4):
#             break
#
#         # 绝对值轮廓的区域    cv2.contourArea为计算轮廓的面积
#         if math.fabs(cv2.contourArea(approx))==0:
#             break
#         print('这是面积：'+str(math.fabs(cv2.contourArea(approx))))
#         if math.fabs(cv2.contourArea(approx)) > 0:
#             if (len(approx) > 4):
#                 # epsilon += Config.epsilon_step
#                 print("epsilon=%d, count=%d"%(epsilon,len(approx)))
#                 continue
#             else:
# #
#                 approx = approx.reshape((4, 2))
#
#                 print('here is the approx:'+approx)
# #                 # 点重排序, [top-left, top-right, bottom-right, bottom-left]
#                 src_rect = order_array(approx)
# #
#                 cv2.drawContours(image, c, -1, (0,255,255),1)
#                 cv2.line(image, (src_rect[0][0],src_rect[0][1]),(src_rect[1][0],src_rect[1][1]),color=(100,255,100))
#                 cv2.line(image, (src_rect[2][0],src_rect[2][1]),(src_rect[1][0],src_rect[1][1]),color=(100,255,100))
#                 cv2.line(image, (src_rect[2][0],src_rect[2][1]),(src_rect[3][0],src_rect[3][1]),color=(100,255,100))
#                 cv2.line(image, (src_rect[0][0],src_rect[0][1]),(src_rect[3][0],src_rect[3][1]),color=(100,255,100))
#
#                 # 获取最小矩形包络
#                 rect = cv2.minAreaRect(approx)
#                 # rect = cv2.maxAreaRect(approx)
#                 box = cv2.boxPoints(rect)
#                 box = np.int0(box)
#                 box = box.reshape(4,2)
#                 box = order_array(box)
#                 print("approx->box")
#                 print(approx)
#                 print(src_rect)
#                 print(box)
#                 w,h = point_distance(box[0],box[1]), \
#                       point_distance(box[1],box[2])
#                 print("w,h=%d,%d"%(w,h))
#
#                 dst_rect = np.array([
#                                     [0, 0],
#                                     [w - 1, 0],
#                                     [w - 1, h - 1],
#                                     [0, h - 1]],
#                                     dtype="float32")
#                 M = cv2.getPerspectiveTransform(src_rect, dst_rect)
#                 warped = cv2.warpPerspective(image, M, (w, h))
#                 cv2.imwrite("transfer%d.png"%idx, warped, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
#                 break

# cv2.imshow("gray_img", gray)
# cv2.imshow("vague_img", binary)
# cv2.imshow("after_binary_img", after_binary)
cv2.imshow("third_binary_img", third_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()