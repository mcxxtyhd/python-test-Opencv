# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ��ˮ���㷨
def water_image():
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)  # ȥ�����

    # gray\binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("binary", binary)

    # morphology operation

    # ����ָ����״�ͳߴ�ĽṹԪ��
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

    # ����������õ�  ������̬ѧ�仯  �ܶ�����
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)

    # �����㣺�ȸ�ʴ�����ͣ���������С����
    # �����㣺�������ٸ�ʴ�������ų�С�ͺڶ�

    # ����  �����Ĳ��ֱ��Ŵ��ˣ��ڰ��Ĳ��ֱ���С
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    # cv.imshow("sure_bg", sure_bg)

    # distance transform
    # ����仯     ��ֵͼ��Ϊ����  ����0 1 ֮��ľ���õ���ͼ�� ͼ����Խ���ĵ㣬�����������ľ���ԽԶ��
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)

    # ��һ��
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("dist_output", dist_output * 70)

    # �ھ���仯 ��ͼ��֮����ж�ֵ��
    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface", surface)

    surface_fg = np.uint8(surface)

    # �õ�����Ľ��
    unknown = cv.subtract(sure_bg, surface_fg)

    # �Ա��¾ɺ��������ڹ���ԭʼͼ���������������С���������½ϴ�����
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