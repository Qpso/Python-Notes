 #! Basic's and aritmetic operations
# Data Types:
# str(value) turns it into a string, meaning a text (can also be called objects)
# int(value) make it into a number
# float(value) into a decimil number
# bool(value) into a boolean which is a true or false
# Built in Functions:
# print is to display text on screen
# can print multiline as follows:
course = '''
Hey this is a multiline comment
it can be written like this
cool right?
'''
print(course) 
# print(10 - 3) will give 7, there is also + for plus, * for multiplication, and / for division
# this is also ** for to the power of, example: 10 ** 3 
# there is a division with // as well that gives an integer as compared to a float from a /
# there is also % that gives the remainder of the division of 10 by 3
# course = "Python for Me"
# you can edit that by using commands like: print(course.upper()) to make it upper case or course.lower for lower case
# course = "Python for me"
#   Index:  012345
# you can also find if there is a letter in a sting, each word is assigned a number like shown above
# print(course.find("y"))
# and that will give 1, you  can also check if a word on letter is in a string with this:
# print("ython" in course)
# but instead of telling you where it'll give you a true or false (boolean value)
# you can also do replace like this:
# print(course.replace("for" , "4"))
# use the comma to indicate what you wanna replace it with
# note that if you are looking for a word in a string instead of a number it'll be something like this:
# course = "Python for me"
# Index:    012345 789
# print(course.find("for"))
# and it'll give you the number 7 instead of 789
# also here's another useful shortcut:
# x = 10
# x = x + 3
# instead of writing that you can write x += 3 which is the same thing as the line above
# there are also things like >, for example writing:
# x = 3 > 2
# print(x)
# it will give a boolean value, there is also >= greater than or equal to, <=, <, == which is equal, not to be confused with =
# and there's != which is not equal too
# to see if a int(eger) is between 2 numbers you can type:
# price = 25
# print( price > 10 and price < 30 ) {returns true if both expressions are true}
# or this also works print( 30 > price > 10 ) 
# there's also print( price > 10 or price < 30 ) and if either price > 10 or price < 30 is true then the whole expression is
# there is also 'not' which can be used as follows:
# print(price > 10) now normally this is false 
# print(not price > 10) {this time assume price is 5} this expression would give a true 
# There's also if, for example: 
temperature = 25 
if temperature > 30: # the : indents it meaning it's part of the if chain
    print("It's a hot day! the temperature is", temperature, "degrees celcius!")
    print("Drink a lot of water!") # and to leave an indentation just press shift+tab 
    # the indentation is called a block of code 
    # there's also elif which is as if and can be looked at as and if 
elif temperature > 20: # this will only give an output if temperature is <30 and > than 20
    print("It's a nice day") 
elif temperature > 10: # will execute if temperature is greater than 10 and less than or equal to 20
    print("It's a bit cold today")
else: # will run if none of the conditions above are true 
    print("It's cold today")
#! While Loops 
# if you want to print, for example, the numbers between 1-5 you can instead of writing them all down with print use while: 
i = 1 
while i <= 5: 
    print(i)
    i += 1 # this will print all numbers till 5 while i is less than or equal to 1:
    # you can see that neat little += 1 instead of i = i + 1 coming in handy there, it's called an augmented  assignment operator 
 # you can also change the output to give a str instead of a number using: 
n = 1 
while n <= 10: 
    print(n * "X") # remember * is multiply 
    n += 1 
    # this will give us X, break line, XX, break line, XXX, and so on until we get to 10 X's
    # side note idk why the XXX is blue 
#! Lists
# we usually have integers, strings, booleans, and floats, but there's also something like lists: 
names = ["Harris", "Bob", "Mosh", "Sam", "Dan"] # use the square brackets for a list
# Index:  0        1      2, etc.
# print(names) will give the exact same thing that names is equal to, with brackets and all
# you can also print specific names using indexes: 
print(names[0]) # will print the first name
# but what if you want to print the last or the second last name in the list, then you can do:
print(names[-1]) # to print the last name, -2 to print the second last, etc. 
# you can also change the name if for example you made a spelling mistake or wanna replace it: 
names[0] = "Haris"
# lists are mutable, so you can change the name if you want, where as normal variables are not mutable unless you assign a new value to it
print(names) # will not print the list with the new name
# however keep in mind since code is top to bottom, the print(names[0]) will still have the old name since it is higher than when we change it
# if you want to get a range of values from the list you can do: 
print(names[0:3]) # this will print the first 3 names, remember 0 is the first name, we entered 0:3 which is the first name to the fourth
# but python will exclude the fourth name and only print what's between it including the first 
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # will add a 6 to the end of the list 
numbers.insert(0, 'W') # insert into the list, the first number is the index and the second is what you want to insert
# above it will insert into the start of the list
numbers.remove(3) # will remove the number 3 from the list 
numbers.pop(2) # will remove the number from the list, put the index in the brackets for the number you want to remove
# there is also other things, for example 
nums1 = [1,2,3,4,5,6,7,8]
max(nums1) # will give the maximum number in the list
min(nums1) # will give the minimum number in the list
del nums1[0:3] # this will delete the values in the list with the index numbers from 0 to 2, since 3 is the end and it wont count
# if you add 2 variables it is assigned like this:
nume1 = 100 # this will have the index number 0 
nume2 = 200 # this will have the index number 1
nume3 = 400 # this will have the index number 2
summary = nume1 + nume2 + nume3 # and summary will have the index number 3
print(len(numbers)) # will count how many elements are in a list and any modifications if put below them
# so for example this will give us 6 since we have W, 1, 2, 4, 5, 6 in the list because of the change's we've made to it 
numbers.clear() # doesnt need any values, will just clear the list
print(numbers)
# but what if you wanna print each item individually, that's where you use a for loop
nums = [1, 2, 3, 4, 5]
for item in nums: #item is our loop variable
    print(item) # in each iteration item will have a diffrent number as it's value, therefore printing all of them in different lines
# you can also do this using the while loop previously shown but it will be a bit longer:
e = 0
while e < len(nums): # you can write len of nums instead of the amount of nums in the list
    print(nums[e])
    e += 1
numeric = range(5) # if you print just this line you'll get 0,5 
for digits in numeric: # but if you add this then you'll get 0,1,2,3,4
    print(digits)  
# and if you add two numbers in it, for example, range(5, 10) 5 will be the start, 10 the end, it'll print numbers between them excluding 10
# can also add a third that'll be used as a step, for example: range(5,10,2)
# it will print 2 numbers at a time from 5, it'll look like this: 5,7,9 
#! Tuples:
# kind of like lists but cant be modified, we use [] for lists and () for tuples 
# you cant modify tuples but you can use .index and .count on it since it only views and doesnt modify 
# formatted strings can be used to visualize a variable easily:
first = 'John'
last = 'Smith'
msg = f'{first} {last} is a coder'
print(msg)
# this will print John Smith is a coder
# this make's it easier to type 
#! Sets 
# sets are kinda like lists, they contain multiple values but are written with {}
# for example 
set = {10, 11, 12, 13, 14}
print(set) # there is a chance that this will change the order the set is written in, althought sometimes you might get the same set multiple times
# the main thing is that set does not support assignment of values, that is to say it wont work with index numbers
# for example if you type set[0] = 9 you will get an error because set doesnt support assignment

#! Built-In Functions 

# there are also many built in functions that we've already used in python like print, int, str, len, etc. 
# built in functions are defined inside the python programming language and can be called from anywhere 
# here are a few examples taken from https://github.com/royalfalcon1146/python/blob/main/main.py
'''
string.replace("n", "m") # a method that outputs the same string but every "n" character is replaced with "m"
     (can be used to remove space between words in a sentence).
string.upper() # a method that outputs the string all in uppercase.
string.lower() # a method that outputs the string all in lowercase.
string.strip() # a method that outputs the string without the surrounding spaces (spaces at the end and beginning).
string.lstrip() # a method that outputs the string without the spaces/indents at the left side.
string.rstrip() # a method that outputs the string without the spaces/indents at the right side.
string.count("e") # a method that outputs the number of times the letter "e" was mentioned in the string.
string.endswith("ing") # a method that checks whether the string ends with "ing" or not, output is boolean.
string.isnumeric() # a method that checks if the string is a numerical value.
string.join(["This", "is", "a", "sentence"]) # a method that outputs the list of words with the string between them.
string.split() # a method that outputs a list of all the words in the string.
if you want input from a user you use it's function as so:
answer = input("What is your answer? ") and you will get an input that will always be a string unless you change it
    if the input you want has to be of just the first character, or first few, or last, etc. you can do:
    answer = input("What is your answer? ")[0] 0 being the index you want, we want the first char so 0, but if you want index 0 to 5 you can do [0:5] etc.
    now if you are writing an equation in it and you want it to understand you can use another function called eval like so:
    eq = input("Enter your equation ") so if you wrote 23+45.3 it will understand and print that
    eq = eval(eq)
    print(eq)
    
if you want to print something a number of time's or write a value a number of times do:
val = (100* "names")


'''

#! Functions
def function(): # this is a function
    print("Hello")
    print("You're so cool")
# leave 2 lines after defining one to make sure it works

function() 

def func(first, last): # first and last are variables in the function
    print(f"Hello {first} {last}")
    print("You're so cool")
# leave 2 lines after defining one to make sure it works

func("Haris", "The Human") # here you enter the values of the variables which is called an argument, this line as a whole is a function call
print(round(1.9546 , 2 )) # rounds a number in it, the comma is how many digits you want after the decimil point

# here's another example using return
def add_numbers(n1,n2):
    result = n1 + n2 # result is just a variable name, it can be anything, any variable inside a function is a local variable and can't be called outside it
    # since local variables are only in a function, you can make another function with the same local variable name  
    return result # returning result takes it outside of the function instead of keeping it in 


number1 = 2.3 # these are our number values
number2 = 4.5 
result = add_numbers(number1, number2) # we could've wrote the values of the number here but it's easier to define the variables and then put it in side

# after putting the values above into add_numbers it goes to n1 and n2 and that is now the value of n1 and n2 respectively 

print("The sum is", result) # also note that once return is used in a function the control goes back to the call and any lines under it are ignored


# contrary to local, we have global variables which can be used anywhere, even outside the function
# global functions are just variables outside a function, we've seen them a lot, example: name = Haris
# but you can also put a global variable INSIDE a function, note however this is a VERY BAD IDEA

messag= "hii" # this is our global variable, it does not require any additional lines to make it global

def greet(nome):
    global messag # here is a global variable inside a function
    messag = "helloo"


greet("Haris")
print(messag) # when printed we will get "helloo" since python reads top to bottom and the global variable in the function comes after the global outside

# now the reason this is a bad pratice is because there might be multiple functions that rely on the value of the first global variable 
# hence changing it inside is a bad idea 

# I've made examples of functions called example 1, it's in the repository.

# here's how to use functions to access certain values, it's called a dictionary.
def save_user(**user):
    print(user["name"]) # the variable inside the square brackets is the value we'll be accessing 


save_user(id=1, name="Haris", age=22) 

# as mentioned earlier, there are functions that are specific to strings, (functions like variable.specificfunction) 
# these are called methods, we've looked at some before, for example the upper function:
test = "Haris" 
print(test.upper()) 
# because this functions is specific to strings, we refer to it as a method 
# this doesn't modify the original string, it just returns the uppercase version of the string, so if you print(test) you should still print Haris
# the variables you have are assigned with an address that is allocated in the memory
# for example to get the address we use:
print(id(nume2)) # which for now will give an id 1630272231888
# but if there are two variables assigned with the same value, they will have the same address 

#! Functions (again)

# A function is a block of code that performs a specific task.
# Functions help to break our program into smaller and modular chunks.
# As our program grows larger and more complex, functions make it more organized and manageable.

# Syntax for defining a function:
# def function_name(parameters):
#     """docstring""" - In Python, a docstring is a string literal that appears as the first statement in a module, class, or function definition.
#                        Its purpose is to document what the code does and how it works.
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



#! Logical Operators
# Have mentioned some of these above but here they are:   
'''
and - used to see if 2 statments are true or false
or - used to see if 1 out of 2 statments are true or false
not - can be used with and to see if one statment is true and one is false
if - used to see if a statment is true or false
else - used with if and is usually used when the opposite of "if" is present 
elif - used with if statment and is just another way of saying else if
'''
# example: 
credit = input("Do you have good credit? (yes/no): ")
income = float(input("What is your monthly income? "))
criminal_record = input("Do you have a criminal record? (yes/no): ")
employment = input("Are you currently employed? (yes/no): ")

if credit.lower() == "yes" and income >= 5000 and not (criminal_record.lower() == "yes") and (employment.lower() == "yes" or income >= 10000):
    print("Congratulations! You qualify for a loan.")
    loan_amount = float(input("How much would you like to borrow? "))
    print("You have been approved for a loan of $" + str(loan_amount) + ".")
elif credit.lower() == "no" or income < 5000 or criminal_record.lower() == "yes" or (employment.lower() == "no" and income < 10000):
    print("Sorry, you do not qualify for a loan.")
else:
    print("Please provide valid input.")

#! Modules and importing them

# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py.
# You can use any Python source file as a module by executing an import statement in some other Python source file.
# When the interpreter encounters an import statement, it imports the module if the module is present in the search path.

# Importing a module
import math

# Now you can use any of the functions in the math module by prefixing them with "math."
# For example:
print(math.sqrt(4))  # Outputs: 2.0

# You can also import specific functions from a module to avoid having to prefix them.
from math import pi, sin

# Now you can use pi and sin directly without prefixing them.
print(pi)  # Outputs: 3.141592653589793
print(sin(0))  # Outputs: 0.0

# You can also import a module under a different name.
import math as m
print(m.sqrt(9))  # Outputs: 3.0

# for more information about the math module visit https://docs.python.org/3/library/math.html 

#! Binary Operation:
bin(3) # will give the binary representation of 3 or a variable you put in (the variable has to have an integer, nothing else)
'''
AND takes the binary of the number and multiplies them (starting from right going left) , use & for and
    example:
        binary rep of 2 = 0010 , it's just 10 but to make it easier we write it in 4 digits also before the 4 digits is 0b, 0 to say it's positive, b=binary
        binary rep of 4 = 0100  , I've not included 0b, oh and if it was negative it'd be -0b
        start with the last digit of each number, so 0x0 is 0, then 1x0 is 0, 0x1 is 0, 0x0 is 0, we get back 0000
        so the if you do print(2&4) you will get 0 since the binary of it is 0000


OR add the binary rep of the numbers (starting from right going left) , use | for or
    example:
        let's use 2 and 4 again:
        binary rep of 2 = 0010 
        binary rep of 4 = 0100
        now we add them, 0 + 0 is 0, 1 + 0 is 1, 0 + 1 is 1, 0 + 0 is 0, we get back 0110 
        so the if you do print(2|4) you will get 6 since the binary of it is 0110
        note that if you get 1 + 1 it will equal to 1 


NOT takes the binary rep of a number and gives the opposite (starting from right going left) , use ~ for not
    example:
        let's use 2 again:
         binary rep of 2 = 0010 
         opposite of 0 is 1, 1 is 0, 0 is 1, 0 again is 1, we get 1101, and the 0b will become -0b
          so if you do print(~2) you will get -3 since the binary of it is 1101

XOR takes the binary rep of 2 numbers and if they are the same, like 0 0 or 1 1 then it will give 0, but if it is diffrent, like 1 0 or 0 1, it will give 1
    example:
        let's use 15 and 2 
        binary rep of 15 is 1111
        binary rep of 2 is 0010
        so (going right to left) 1 0 is 1, 1 1 is 0, 1 0, is 1 and again 1 0 is 1, so we get 1101
        so if you print(15^2) you will get 13 since 1101 is it's binary rep

'''


