import os
import cv2
from math import *

class rotateImg:

    def __init__(self,target_degree,in_path,out_path):
        self.target_degree = target_degree
        self.in_path = in_path
        self.out_path = out_path

    '''
    target_degree:逆时针旋转的角度
    in_path：需要转换的图片文件夹
    out_path：需要输出的图片文件夹
    '''
    def deal_butch_img(self):
        all_files_paths,all_filenames=self.get_AllImgsDir(self.in_path)

        for i in range(len(all_files_paths)):
            out_filenames=str(self.out_path)+"/"+str(all_filenames[i])
            self.rotate_img(self.target_degree,all_files_paths[i],out_filenames)

    '''
    获得指定目录的所有文件
    file_path:文件地址
    '''
    # 拼凑所有的文件地址
    def get_AllImgsDir(self,file_path):
        files = os.listdir(file_path)

        files_paths=[]
        files_names=[]

        for singlefile in files:

            target_file_path=str(file_path)+"/"+str(singlefile)

            files_paths.append(target_file_path)
            files_names.append(singlefile)

        return files_paths,files_names

    '''
    处理制定路径的照片
    target_degree:逆时针旋转的角度
    in_path：需要转换的图片文件夹
    out_path：需要输出的图片文件夹
    '''
    def rotate_img(self,target_degree,in_path,out_path):

        print('正在处理照片：'+str(in_path))

        img = cv2.imread(in_path)

        # 获得长宽
        height,width=img.shape[:2]

        # 获得新的长宽
        heightNew=int(width*fabs(sin(radians(target_degree)))+height*fabs(cos(radians(target_degree))))
        widthNew=int(height*fabs(sin(radians(target_degree)))+width*fabs(cos(radians(target_degree))))

        matRotation=cv2.getRotationMatrix2D((width/2,height/2),target_degree,1)

        matRotation[0,2] +=(widthNew-width)/2
        matRotation[1,2] +=(heightNew-height)/2

        # 生成图片
        imgRotation=cv2.warpAffine(img,matRotation,(widthNew,heightNew),borderValue=(255,255,255))

        cv2.imwrite(out_path,imgRotation)

        print('照片处理完毕，输出目录为：' + str(out_path))

if __name__ == "__main__":
    pass

    # 示例
    # theotest=rotateImg(90,r"C:\Users\mcxxt\Desktop\org_img",r"C:\Users\mcxxt\Desktop\convert_img")
    # theotest.deal_butch_img()


