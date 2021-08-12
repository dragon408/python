array = []

print("Enter the elements of the array.")
print("At the end, enter 0")
main = True
while main:
    element = input()
    if element != "0":
        array.append(element)
    else:
        main = False

a = input("Output an array?y/n ")
if a == "y":
    for i in range(len(array)):
        print(array[i], end = " ")
else:
    pass
