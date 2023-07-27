# 1. Declare two variables, `num1` and `num2`, and assign them with integer values.
num1 = 5
num2 = 10

# 2. Write a program that checks if `num1` is greater than `num2` and prints the result.
def is_greater(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")

# 3. Use an `if-else` statement to determine if the values of `num1` and `num2` are equal or not, and print an appropriate message.

def is_equal(num1, num2):
    if num1 == num2:
        print(f"{num1} is equal to {num2}")
    else:
        print(f"{num1} is not equal to {num2}")

# 4. Prompt the user to enter a number and store it in a variable.
user_input = input("Enter a number: ")

# 5. Use a loop to print all the numbers from 1 to the user-input number.
def print_nums(num):
    for i in range(1, num + 1):
        print(i)
# Test functions
print("Running tests")
# Test the function is_greater
# When num1 is greater than num2
num1 = 5
num2 = 2

# Prints "5 is greater than 2"
 
is_greater(num1, num2) == "5 is greater than 2"

# When num1 is not greater than num2
num1 = 2
num2 = 5

# Prints "{num1} is not greater than {num2}"
is_greater(num1, num2) == "2 is not greater than 5"

# Test the function is_equal
# When num1 is equal to num2
num1 = 5
num2 = 5

# Prints "{num1} is equal to {num2}"
is_equal(num1, num2) == "5 is equal to 5"

# When num1 is not equal to num2
num1 = 2
num2 = 5

# Prints "{num1} is not equal to {num2}"
is_equal(num1, num2) == "2 is not equal to 5"

# Test the function print_nums
# When num is 5
num = 5
# Print the numbers from 1 to 5
print_nums(num)