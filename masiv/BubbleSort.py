from random import randint #library for random numbers


def bubble(array): #sort function
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 10
a = []
for i in range(N): #filling the array with random numbers
    a.append(randint(1, 99))

print(a) #outputting the original array
bubble(a) #sorting (function call)
print(a) #sorted array output