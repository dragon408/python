def print_operation():
    print("Select an operation:")
    print("1 - plus")
    print("2 - minus")
    print("3 - multiplication")
    print("4 - division")

def calculator(n1, n2, operation):
    if operation == 1:
        res = int(n1 + n2)
        print("Result = ", res)
    elif operation == 2:
        res = int(n1 - n2)
        print("Result = ", res)
    elif operation == 3:
        res = int(n1 * n2)
        print("Result = ", res)
    elif operation == 4:
        res = int(n1 / n2)
        print("Result = ", res)
    else:
        print("Invalid input ")

main_func = True

while main_func:
    try:
        number1, number2 = input("Enter two numbers separated by a space ").split()
        print_operation()
        operation = int(input())
        calculator(int(number1), int(number2), operation)
        a = input("Anew: y/n ")
        if a == "y":
            pass
        else:
            print("Thank, goodbye")
            main_func = False
    except Exception as ex:
        print(ex)



