# just here to test random code
# yes it's supposed to be empty (usually)

# Functions

# A function is a block of code that performs a specific task.
# Functions help to break our program into smaller and modular chunks.
# As our program grows larger and more complex, functions make it more organized and manageable.

# Syntax for defining a function:
# def function_name(parameters):
#     """docstring"""
#     statement(s)

# Here is an example of a function that takes in two parameters and returns their sum:

def add_numbers(num1, num2):
    """
    This function takes in two numbers and returns their sum.
    """
    return num1 + num2

# We can now call the function by passing in two numbers as arguments:
sum_of_nums = add_numbers(3, 5)
print(sum_of_nums)  # Output: 8

# Here is an example of a function that takes in a list of numbers and returns their average:

def calculate_average(numbers):
    """
    This function takes in a list of numbers and returns their average.
    """
    total_sum = sum(numbers)
    length = len(numbers)
    return total_sum / length

# We can now call the function by passing in a list of numbers as an argument:
num_list = [4, 5, 6, 7, 8]
avg_of_nums = calculate_average(num_list)
print(avg_of_nums)  # Output: 6.0

# We can also call the function by passing in a tuple of numbers as an argument:
num_tuple = (4, 5, 6, 7, 8)
avg_of_nums = calculate_average(num_tuple)
print(avg_of_nums)  # Output: 6.0

# We can also call the function by passing in a set of numbers as an argument:
num_set = {4, 5, 6, 7, 8}
avg_of_nums = calculate_average(num_set)
print(avg_of_nums)  # Output: 6.0
