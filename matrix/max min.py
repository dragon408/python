import numpy as np

arr = np.array([[3,3],[2,5]])
min = arr[0][0]
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if min > arr[i][j]:
            min = arr[i][j]
print("min: ", min)

#or

arr1 = np.array([[3,3],[2,5]])
min = np.amin(arr1)
max = np.amax(arr1)
print("min: ", min)
print("max: ", max)