import numpy as np
import math

# 计算一批数据的方法
def calculate_result(in_x,in_y,in_z,in_num):

    xmat = np.array(in_x)
    ymat = np.array(in_y)
    zmat = np.array(in_z)

    i=0
    j=0
    CC1=0
    CC2=0
    CC3=0

    # 最后一行的数据不算
    while (i<in_num-1):
        j=i+1
        while (j<in_num):
            D=math.pow((xmat[i]-xmat[j]),2)+math.pow((ymat[i]-ymat[j]),2)+math.pow((zmat[i]-zmat[j]),2)
            d=math.sqrt(D)
            j= j+1
            if (d>1.54):
              continue
            elif (1.44 < d <=1.54):
               CC1=CC1+1
            elif (1.27<d<=1.44):
               CC2=CC2+1
            elif (d<=1.27):
               CC3=CC3+1
        else:i=i+1

    print('Here are the results:')
    print('CC1=',CC1)
    print('CC2=',CC2)
    print('CC3=',CC3)
    print('')


f = open('CCBJ3.txt','r')
lines = f.readlines()

x=[]
y=[]
z=[]
num_batch=0
target_string="Generated"

for single_item in lines:

    # # 1、查找制定的字符串
    # if target_string in str(single_item):
        # print(single_item)

    # 2、数据清理
    line = single_item.strip().split()

    if len(line)==7:
        # 数量增加1
        num_batch+=1

        x.append(float(line[2]))
        y.append(float(line[3]))
        z.append(float(line[4]))

        # 等于3000时计算
        if num_batch == 3000:
            calculate_result(x, y, z, num_batch)
    else:
        # 碰到了截断点
        num_batch = 0
        x.clear()
        y.clear()
        z.clear()
        print(single_item)


