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

cap=cv2.VideoCapture(0)
# 创建检测人脸的对象 要在opencv的目录下找到xml文件，放置到自己项目中

# 检测人脸
face_cascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")
# 检测眼睛
eye_cascade = cv2.CascadeClassifier("../haarcascades/haarcascade_eye.xml")


while True:
    #从摄像头读取图片
    sucess,img=cap.read()
    # 1、首先转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 进行人脸检测
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print('人脸：')
    print(faces)
    for (x, y, w, h) in faces:
        # 画出矩形框
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 进行双眼检测
        roi_gray=gray[y:y+h,x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5,0,(40,40))

        print('眼睛：')
        print(eyes)
        for (ex,ey,ew,eh) in eyes:
            # 画出矩形框
            cv2.rectangle(img,(ex+x,ey+y),(ex+ew+x,ey+eh+y),(255,0,0))

    cv2.imshow("humanRe", img)

    #保持画面的持续。
    k=cv2.waitKey(1)

    if k == 27:
        #通过esc键退出摄像
        cv2.destroyAllWindows()
        break

#关闭摄像头
cap.release()