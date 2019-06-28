import numpy as np

arr = np.arange(10)
print(arr)

arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
print(arr_slice)

arr_slice[1] = 12345

print(arr)
# array([ 6. ,  7.5,  8. ,  0. ,  1. ])