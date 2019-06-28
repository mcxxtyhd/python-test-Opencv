import cv2
import numpy as np


# 用训练好的数据（yml文件）创建一个识别器对象
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')

# 检测人脸
cascade_path = "../haarcascades/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# 调用摄像头
cam = cv2.VideoCapture(0)

# 显示的字体
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    # 正常操作  检测人像
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:

        # 这是经过修饰的结果 为了表明人像检测的区域(扩大了人像检测的区域)
        cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (0, 225, 0), 2)
        # 这是正常检测出来的结果
        # cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 这是人像识别的精华  用训练的数据加载的识别器   同摄像头获取的图像进行对比  得出结论
        img_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        # 这个结果是相似度  不同于其他几个算法  不同算法不同考量

        # 这里之后去调查  应该是置信度越低越好  通常50作为标准的分界线
        if conf < 50:
            # id参数需要根据实际进行设置
            if img_id == 3:
                img_id = 'theo'
            elif img_id == 2:
                img_id = 'ghost'
        else:
            img_id = "Unknown"
        # cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)

        # 这个是输出识别的字体  就是那一行字
        cv2.putText(im, str(img_id), (x, y + h), font, 0.55, (0, 255, 0), 1)


    cv2.imshow('im', im)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
