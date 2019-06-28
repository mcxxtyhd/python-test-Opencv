import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('3.jpg')
rows, cols = img.shape[:2]

# 原图中卡片的四个角点
pts1 = np.float32([[148, 80], [437, 114], [94, 247], [423, 288]])
# 变换后分别在左上、右上、左下、右下四个点
pts2 = np.float32([[0, 0], [320, 0], [0, 178], [320, 178]])

# 生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)
# 进行透视变换
dst = cv2.warpPerspective(img, M, (320, 178))

cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()