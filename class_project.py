# simple calculator

# The calculator must be a function

def calculator():
    """This is a basic calculator"""

    print("This is a simple calculator, and it can perform simple arithmetic")

    num1 = int(input("Enter your first number"))
    num2 = int(input("Enter your second number"))

    print("Please select any operation")
    print(" ")

    print("Choose 1, for addition")
    print("Choose 2, for subtraction")
    print("Choose 3, for division")
    print("Choose 4, for multiplacation")

    operation = input("Enter one above options")

    if operation == "1":
        result = num1 + num2
        print(result)
    elif operation == "2":
        result = num1 - num2
        print(result)
    elif operation == "3":
        try:
            result = num1 / num2
            print(result)
        except ZeroDivisionError:
            print("Error: It is not allowed to divide by zero")
    elif operation == "4":
        result = num1 * num2
        print(result)

    else:
        print("INVALID OPERATION")

    repeat = input("Do you want to perform another operation").lower()

    if repeat == "yes":
        calculator()
    else:
        print("Good Bye")


calculator()

    
    
# This is a basic calcuator
# 
# 
# ask for num1
# ask for num2
# 
# print("choose on operation")
# print("")
# print("1. Addition")
# 
# 
# operation = input("Chooose the operation you would ")    

# if operation = "1" : add num1 and num2
# if operation = "2" : minus num2 from num1
# if operation = "3" : divide num1 by num2 , try and except 
# if operation = "4" : multiply num1 by num2

# else: invalid

# again = input("Do you want to perform another operation").lower() 
# if again == "yes":
# calculator()
# else: print(gppdbye)

