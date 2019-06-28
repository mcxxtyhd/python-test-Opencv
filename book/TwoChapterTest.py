# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture("test.avi")
while True:
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()