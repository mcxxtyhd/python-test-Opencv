import cv2

import numpy as np

cz_img=cv2.imread("img/cz.jpg")

gray = cv2.cvtColor(cz_img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("img/gray_cz.jpg",gray)

for single in range(len(gray)):
    gray[single]=255
    # print(single)

cv2.imshow('theo',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(gray)

# mask_all = np.zeros((500, 500), dtype='uint8')
# mask_all=np.full((500,500),255)
#
# print(mask_all)
#
#
# cv2.imshow('theo',mask_all)
# cv2.waitKey(0)
# cv2.destroyAllWindows()