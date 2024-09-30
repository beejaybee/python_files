# Write a program that ask for user for two inputs
# check if the numbers are even or odd
# then add the numbers

def check_even_odd(num):
    if num % 2 == 1:
        print("You've entered an odd num")
    else:
        print("You've entered an even number")


print("Enter your first number")
first_num = input()
check_even_odd(int(first_num))




print("Enter the second number")
second_num = input()
check_even_odd(int(second_num))


print(int(first_num) + int(second_num))