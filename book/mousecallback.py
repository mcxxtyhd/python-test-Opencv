import cv2
import numpy as np


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:  # 处理鼠标左键双击
        print('x:'+str(x)+',y:'+str(y))
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)  # 在鼠标点击位置创建圆


# 创建一个黑背景图像
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)  # 设置回调函数

while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:  # esc键退出
        break
cv2.destroyAllWindows()