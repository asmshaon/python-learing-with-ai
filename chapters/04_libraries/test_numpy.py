# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(2, 3, 2)

# print(newarr)

# [[1 2 3]  [4 5 6] [7 8 9] [10 11 12]] - 2 D

# [[[1, 2] [3, 4] [5 6]] , [[7 8] [9 10] [11 12]]]

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# print(arr.reshape(2, 4).base)

import numpy as np

# arr = np.array([1, 2, 3])

# for x in arr:
#     print(x)


# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#     print(x)


# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#     for y in x:
#         print(y)


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#     print(x)
#     print("***" * 10)


import numpy as np

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#     print(x)
#     print("***" * 10)


# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
#     print(x)


# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for x in np.nditer(arr[:, ::2]):
#     print(x)


# arr = np.array([1, 2, 3])

# for idx, x in np.ndenumerate(arr):
#     print(idx, x)


# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for idx, x in np.ndenumerate(arr):
#     print(idx, x)


# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1, arr2))

# print(arr)


# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=1)

# print(arr)


# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)


# arr = np.array([1, 3, 5, 7])

# x = np.searchsorted(arr, [2, 4, 6])

# print(x)

import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#     # if the element is completely divisble by 2, set the value to True, otherwise False
#     if element % 2 == 0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# filter_arr = arr % 2 == 0

# print(arr[filter_arr])

# data = np.random.normal(50, 10, 1000)


# print(data)


# ddd = np.random.normal(1, 10, 3)

# print(ddd)


# arr_float = np.array(["ABC", 2.0, 3.0])

# print(arr_float.dtype)


# ze = np.zeros(4, dtype=np.int32)

# print(ze)


import numpy as np
import time

size = 10

start = time.time()

python_list = list[size](range(size))

[l * 1 for l in python_list]

time_python = time.time() - start

print(f"{time_python:.6f} - {len(python_list)}")

# Numpy list

start = time.time()

numpy_list = np.arange(size)

result_numpy = [int(x + 1) for x in numpy_list]

time_numpy = time.time() - start

print(f"{time_numpy:.6f} - {len(numpy_list)}")

print(f"Numpy is {time_python/time_numpy:.1f}x fastr")

print(python_list)
print(result_numpy)
