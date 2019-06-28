"""
:param
    无
:return
    无
功能：调用笔记本摄像头获取视频图片
"""""
import numpy as np
import cv2
#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
from demo_getRect.utils import point_distance, get_nowstime_str

cap=cv2.VideoCapture(1)

# cap.set(3,1366)
# cap.set(4,768)

# fps =cap.get(cv2.CAP_PROP_BRIGHTNESS)
# print("这是帧数："+str(fps))
# cap.set(5,30)

while True:
    #从摄像头读取图片
    sucess,img=cap.read()
    # 1、首先转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2、之后进行滤波模糊
    binary = cv2.medianBlur(gray, 51)

    # 3、转换为二值图像
    ret, after_binary = cv2.threshold(binary, 91, 255, cv2.THRESH_BINARY)

    # 4、提取轮廓
    _, contours, _ = cv2.findContours(after_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    target_rect_area=[]

    for single_item in contours:

        rect = cv2.minAreaRect(single_item)  # 找到最小矩形区域

        box = cv2.boxPoints(rect)  # 找到最小矩形的顶点
        # 取整
        box = np.int0(box)

        target_rect_area.append(box)

        cv2.drawContours(img, [box], 0, (0, 255, 0), 4)

    #显示摄像头，背景是灰度。
    cv2.imshow("img",img)
    #保持画面的持续。
    k=cv2.waitKey(1)
    if k == 27:
        #通过esc键退出摄像
        cv2.destroyAllWindows()
        break
    elif k==ord("s"):

        if len(target_rect_area)==1:
            # 计算长和宽

            mine_height, mine_length = point_distance(target_rect_area[0][0], target_rect_area[0][1]), point_distance(target_rect_area[0][1], target_rect_area[0][2])

            # 原图中卡片的四个角点    绿  红  黑  蓝
            target_img = np.float32([target_rect_area[0][1], target_rect_area[0][0], target_rect_area[0][3], target_rect_area[0][2]])

            new_img = np.float32([[0, 0], [0, mine_height], [mine_length, mine_height], [mine_length, 0]])

            # 生成透视变换矩阵
            M = cv2.getPerspectiveTransform(target_img, new_img)
            # 进行透视变换
            dst = cv2.warpPerspective(img, M, (int(mine_length), int(mine_height)))

            print("这是图片的名称："+get_nowstime_str())

            imgname="imgstore/"+get_nowstime_str()+".jpg"
            cv2.imwrite(imgname, dst)

            # 然后接着分
            if mine_height>mine_length:
                pass


        #通过s键保存图片，并退出。
        # cv2.imwrite("image2.jpg",img)
        # cv2.destroyAllWindows()
        # break
        continue
#关闭摄像头
cap.release()