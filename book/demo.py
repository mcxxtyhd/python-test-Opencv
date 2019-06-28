import cv2

imgpath = "../img/cz.jpg"

img = cv2.imread(imgpath)

print(img[100,100])

# img[300:400,300:400,0]=255

# cv2.imwrite("../img/newcardemo.png",img0)

cv2.imshow("Image",img)

cv2.waitKey(0)