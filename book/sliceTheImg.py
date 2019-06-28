import cv2
import datetime

from numpy import int0

myimg=cv2.imread("img/cz.jpg")
height,width=myimg.shape[:2]

per_num=3

per_height=int0(height/per_num)
per_width=int0(width/per_num)

print(str(per_height))
print(str(per_width))

plug_height=0
for x_item in range(per_num):

    plug_width = 0
    for y_item in range(per_num):
        new_img=myimg[plug_height:plug_height+per_height,plug_width:plug_width+per_width]
        cv2.imshow("img"+str(x_item)+'_'+str(y_item),new_img)
        plug_width += per_width

    plug_height+=per_height

cv2.waitKey(0)
cv2.destroyAllWindows()

# frame = myimg[120:360, 160:480]#切割区域
# cv2.imwrite(path + str(c) + '.jpg', frame)  # 存储图像