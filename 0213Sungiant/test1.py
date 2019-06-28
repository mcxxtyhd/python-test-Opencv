#!/usr/bin/python3
# 2018.01.17 22:36:20 CST
import cv2
import numpy as np
import time

img = cv2.imread('test1.jpg', 0)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # ensure binary
retval, labels = cv2.connectedComponents(img)

##################################################
ts = time.time()
num = labels.max()

N = 50
for i in range(1, num+1):
    pts =  np.where(labels == i)
    if len(pts[0]) < N:
        labels[pts] = 0

print("Time passed: {:.3f} ms".format(1000*(time.time()-ts)))
# Time passed: 4.607 ms

##################################################

# Map component labels to hue val
label_hue = np.uint8(179*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

# cvt to BGR for display
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

# set bg label to black
labeled_img[label_hue==0] = 0

cv2.imshow('labeled.png', labeled_img)
cv2.imwrite("labeled.png", labeled_img)
cv2.waitKey()