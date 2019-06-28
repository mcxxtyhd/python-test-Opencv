import cv2
import numpy as np

# 读取图片
org_img=cv2.imread("cell.jpg",0)

cv2.imshow("org_img",org_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

