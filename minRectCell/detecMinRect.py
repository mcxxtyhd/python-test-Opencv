import cv2
import numpy as np

from minRectCell.img_rect import cell_rect

def detect_theminiest_rect(img):
    # 1、首先转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2、转换为二值图像
    ret, after_binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # 3、提取轮廓
    _, contours, _ = cv2.findContours(after_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow("after_binary", after_binary)

    # 确保轮廓只有一个
    if len(contours)>0:

        # 找出最大面积的轮廓 的 索引号
        max_area_num=-1
        now_area=0
        big_area=0
        for item in range(len(contours)):
            now_area=cv2.contourArea(contours[item])
            if now_area>big_area:
                big_area=now_area
                max_area_num=item

        # 赋予计算最大面积的轮廓
        target_contour=contours[max_area_num]

        # 现在要找打面积最大的轮廓
        xm,ym,w,h= cv2.boundingRect(target_contour)  # 找到最小包围框

        # box = cv2.boxPoints(rect)  # 找到最小矩形的顶点
        # # 取整
        # box = np.int0(box)

        # 修正误差
        error=5
        # 考虑到0的情况
        if xm-error<0:
            xmin=0
        else:
            xmin = xm - error
        xmax = xm+w+error
        # 考虑到0的情况
        if ym - error<0:
            ymin=0
        else:
            ymin = ym - error
        ymax = ym+h+error
        new_rect = cell_rect(xmin, xmax, ymin, ymax, '')

        # cv2.rectangle(img,(xm-error,ym-error),(xm+w+error,ym+h+error),(255,255,255),1)
        # cv2.drawContours(img, [box], 0, (255, 255, 255), 1)
        # cv2.imshow("org", img)

        return new_rect
    else:
        return 'ErrorCell'

# img_cell=cv2.imread('cell2.jpg')
# test_rect=detect_theminiest_rect(img_cell)
# print(test_rect.__str__())


# cv2.waitKey(0)
# cv2.destroyAllWindows()