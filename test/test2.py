#保存图片
import cv2
cap = cv2.VideoCapture(0)
i=0
while(1):
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        i=i+1
        imgName="i_"+str(i)
        cv2.imwrite("img/"+imgName+".jpeg", frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
cap.release()
cv2.destroyAllWindows()