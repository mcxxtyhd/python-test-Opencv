import numpy as np
import matplotlib.pyplot as plt

x_data=[1.0,2.0,3.0]
y_data=[2.0,4.0,6.0]

def forword(x):
    return x*w

def loss(x,y):
    y_pred=forword(x)
    return (y_pred-y)*(y_pred-y)

def gradient(x,y):
    return 2*x*(x*w-y)

w_list=[]
mse_list=[]

for w in np.arange(0.0,4.1,0.1):
    print("w=",w)
    l_sum=0

    for x_val,y_val in zip(x_data,y_data):
        y_pred=forword(x_val)
        l=loss(x_val,y_val)
        l_sum+=l
        print("\t",x_val,y_val,y_pred,l)

    print("NSE=",l_sum/3)
    w_list.append(w)
    mse_list.append(l_sum/3)

plt.plot(w_list,mse_list)
plt.ylabel('loss')
plt.xlabel('w')
plt.show()