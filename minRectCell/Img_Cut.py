import os

import cv2

from minRectCell.Img_Get_Info import get_cell_rect

# xml文件地址
xml_path='cellTwo.xml'
# 读取xml文件信息
img_path,point_location=get_cell_rect(xml_path)
# 读取图片
img=cv2.imread(img_path)

# 创建文件夹保存所有的cell图
save_dir_path=xml_path[0:len(xml_path)-4]
os.makedirs(save_dir_path)

# 遍历每个细胞进行保存
for single_point in point_location:
    label_area=single_point

    # 这是就对应标注的某个细胞
    new_img=img[label_area.ymin:label_area.ymax,label_area.xmin:label_area.xmax]

    # 拼凑每个细胞的名称 进行保存
    img_name=str(label_area.labelname)+"_"+str(label_area.xmin)+"_"+str(label_area.xmax)+"_"+str(label_area.ymin)+"_"+str(label_area.ymax)+".jpg"
    new_img_path=save_dir_path+'/'+img_name
    cv2.imwrite(new_img_path,new_img)

# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
