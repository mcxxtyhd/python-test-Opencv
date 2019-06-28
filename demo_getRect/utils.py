import datetime
import math

import numpy as np

def get_nowstime_str():
    now_time = datetime.datetime.now()
    nowtime_str=str(now_time)
    nowtime_str=nowtime_str.replace("-","").replace(" ","").replace(":","").replace(".","")
    return str(nowtime_str)


def point_distance(p1,p2):
    x_distance=math.fabs(p2[0]-p1[0])
    y_distance=math.fabs(p2[1]-p1[1])

    return math.sqrt(x_distance*x_distance+y_distance*y_distance)


def order_array(test_array):
    test_array = np.array(test_array)
    test_array=test_array.reshape(4,2)
    x1=test_array[0][0]
    x2=test_array[1][0]
    x3=test_array[2][0]
    x4=test_array[3][0]
    y1=test_array[0][1]
    y2=test_array[1][1]
    y3=test_array[2][1]
    y4=test_array[3][1]

    x_list=([x1,x2,x3,x4])
    y_list=([y1,y2,y3,y4])

    x_min=min(x_list)
    x_max=max(x_list)
    y_min=min(y_list)
    y_max=max(y_list)

    test_array[0][0]=x_min
    test_array[1][0]=x_max
    test_array[2][0]=x_max
    test_array[3][0]=x_min
    test_array[0][1]=y_min
    test_array[1][1]=y_min
    test_array[2][1]=y_max
    test_array[3][1]=y_max

    return test_array






