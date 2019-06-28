import cv2

img = cv2.imread('theoimg.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
_,contours, hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


length = len(contours)
print (length)
for i in range(length):

    cnt = contours[i]

    # epsilon = 0.00001 * cv2.arcLength(cnt,True)
    epsilon = 0.01

    # 对图像轮廓点进行多边形拟合
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # cv2.drawContours(img, approx, -1, (0, 0, 255), 3)

    # print('here is the len:'+str(len(approx)))
    # print('this is the point:'+str(approx))
    #
    #
    # print('test:'+str(approx[0]))
    # print('test:' + str(approx[0][0]))
    # print('test:' + str(approx[0][0][1]))

    cv2.polylines(img, [approx], True, (0, 0, 255), 2)

    cv2.imshow("approx",img)

cv2.waitKey(0)