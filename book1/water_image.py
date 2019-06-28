# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 分水岭算法
def water_image():
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)  # 去除噪点

    # gray\binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("binary", binary)

    # morphology operation

    # 返回指定形状和尺寸的结构元素
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

    # 根据上述获得的  进行形态学变化  很多隽星
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)

    # 开运算：先腐蚀再膨胀，用来消除小物体
    # 闭运算：先膨胀再腐蚀，用于排除小型黑洞

    # 膨胀  光亮的部分被放大了，黑暗的部分被缩小
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    # cv.imshow("sure_bg", sure_bg)

    # distance transform
    # 距离变化     二值图像为基础  计算0 1 之间的距离得到的图像 图像上越亮的点，代表了离零点的距离越远。
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)

    # 归一化
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("dist_output", dist_output * 70)

    # 在距离变化 的图像之后进行二值化
    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface", surface)

    surface_fg = np.uint8(surface)

    # 得到相减的结果
    unknown = cv.subtract(sure_bg, surface_fg)

    # 对比新旧函数，用于过滤原始图像中轮廓分析后较小的区域，留下较大区域
    ret, markers = cv.connectedComponents(surface_fg)
    print('here is the ret:'+str(ret))

    # watershed transfrom
    markers += 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 255, 0]
    cv.imshow("result", src)


src = cv.imread("coin.jpg")
cv.imshow("org_img", src)
water_image()
cv.waitKey(0)
cv.destroyAllWindows()