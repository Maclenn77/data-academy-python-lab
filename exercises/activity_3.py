# Create a list of integers containing at least 10 elements.
list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Write a function that takes the list as input and returns the maximum and minimum values.
def max_and_min(list_of_ints):
    max_value = max(list_of_ints)
    min_value = min(list_of_ints)
    return max_value, min_value

# Write a function that takes the list as input and returns the average.
def calculate_average(list_of_ints):
    total = sum(list_of_ints)
    return total / len(list_of_ints)

# Implement a function that reverses the order of the elements in the list.
def reverse_list(list_of_ints):
    return list_of_ints[::-1]

# Write a function that searches for a given value in the list and returns its index.
def search(list_of_ints, value):
    return list_of_ints.index(value)

# Implement a function that takes a list of numbers and returns a new list with only the even numbers.
def even_numbers(list_of_ints):
    return [num for num in list_of_ints if num % 2 == 0]

# Test functions
print("Running tests")
# Test the function max_and_min
print("When the list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], max_and_min should return (10, 1)")
max_value, min_value = max_and_min(list_of_ints)
print(max_value == 10 and min_value == 1)
# Test the function calculate_average
print("When the list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], calculate_average should return 5.5")
print(calculate_average(list_of_ints) == 5.5)
# Test the function reverse_list
print("When the list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reverse_list should return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]")
print(reverse_list(list_of_ints) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# Test the function search
print("When the list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and the value is 5, search should return 4")
print(search(list_of_ints, 5) == 4)
