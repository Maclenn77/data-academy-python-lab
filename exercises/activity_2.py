import os

# Write a function that takes two parameters, `num1` and `num2`, and returns their sum.
def add(num1, num2):
    return num1 + num2

# Create a text file named "numbers.txt" and write a few numbers, each on a new line.
with open("numbers.txt", "w") as f:
    f.write("1\n")
    f.write("2\n")
    f.write("3\n")
    f.write("4\n")
    f.write("5\n")

# Write a function that reads the numbers from the file and calculates their average.
def calculate_average():
    with open("numbers.txt", "r") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            try:
                total += int(line)
            except ValueError:
                continue
        return total / len(lines)

# Implement a function that takes a string as input and writes it to the end of the "numbers.txt" file.
def write_to_file(string):
    with open("numbers.txt", "a") as f:
        f.write(string)

# Call the functions and print the results.
print(add(5, 10))
print(calculate_average())
write_to_file("Hello World")

with open("numbers.txt", "r") as f:
    lines = f.readlines()
    print("File contains: \n" + "".join(lines))

# Remove hello world from the file
with open("numbers.txt", "r") as f:
    lines = f.readlines()
    lines = lines[:-1]
    with open("numbers.txt", "w") as f2:
        f2.writelines(lines)


# Test functions
print("Running tests")
# Test the function add
# When num1 is 5 and num2 is 10
num1 = 5
num2 = 10
# Returns 15
print("When num1 is 5 and num2 is 10, add should return 15")
print(add(num1, num2) == 15)

# Test the function calculate_average
# When the file contains the numbers 1, 2, 3, 4, 5
# Returns 3.0
print("When the file contains the numbers 1, 2, 3, 4, 5, calculate average should return 3.0")
print(calculate_average() == 3.0)

# Test the function write_to_file
# When the string is "Hello World"
write_to_file("Hello World")

# Last line of the file should be "Hello World"
print("Last line of the file should be 'Hello World'")
with open("numbers.txt", "r") as f:
    lines = f.readlines()
    print(lines[-1] == "Hello World")

# Delete the file
os.remove("numbers.txt")
    
