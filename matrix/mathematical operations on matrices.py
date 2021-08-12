import numpy as np

arr1 = np.array([[3,3,3],[2,5,5]])
arr2 = np.array([[2,4,2],[1,3,8]])
temp = arr1 + arr2
print(temp)


arr1 = np.array([[3,3],[2,5]])
arr2 = np.array([[2,4],[1,3]])
temp = arr1.dot(arr2)
print(temp)