import numpy as np

arr1 = np.array([[3,3],[2,5]])
temp = arr1.transpose()
print(temp)


a = 10
b = 5

if a % 4 - a // 4 > 0:
    print(1)
else:
    print(a % b)