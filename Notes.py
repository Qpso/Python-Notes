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

j=0

days = ['Sunday' , 'Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday']
while j<len(days): # here you dont have to count the list and then put a number, just use len and it will print it all
    print(days[j]) # instead of writing the index number of all the days in the list, we can just use j, starting at 0 for index 0, and add till len(days)
    j = j + 1

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
def save_user(**user): #the two *'s are called kwags, key word arguments        
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

#! For Loops

# Example of a for loop that iterates over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example of a for loop that generates a sequence of numbers using range()
for i in range(1, 5):
    print(i)

# Example of a for loop that uses enumerate() to get the index and value of each item in a list
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Example of a for loop with a conditional statement to filter items in a list
numbers = [1, 2, 3, 4, 5]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# Here's why we did even_numbers = [] above:

# Example of a for loop with a conditional statement to filter items in a list
numbero = [1, 2, 3, 4, 5]

# Initialize an empty list to store the even numbers that we find
even_numbero = []

# Iterate over each number in the list and check if it's even
for num in numbero:
    if num % 2 == 0:
        # If the number is even, append it to the even_numbers list
        even_numbero.append(num)

# Print the even_numbers list
print(even_numbero)

# Nested for loop to print pattern
for i in range(4):
    for j in range(4):
        # Print '#' character with end='' to print on the same line
        print("#", end="")
    
    # Print empty string to move to the next line
    print()


"""

In this code, we have a nested for loop. The outer for loop iterates over the range of numbers from 0 to 3 (inclusive) using `range(4)`.
This loop controls the number of rows in the pattern. The inner for loop also iterates over the range of numbers from 0 to 3 (inclusive) using `range(4)`.
This loop controls the number of columns in the pattern.
 Inside the inner loop, we print the '#' character using the `print()` function with the `end` parameter set to an empty string (`end=""`).
The `end` parameter specifies what should be printed at the end of the string instead of the default newline character.
 By setting it to an empty string, we ensure that each '#' character is printed on the same line. 
After the inner loop finishes, we print an empty string using `print()` again,
 which causes a newline character to be printed and moves us to the next row in the pattern. 

""" 

#! Some more bult-in Functions 

inputs = input("Enter a few values seperated by a ,: ")

L = inputs.split(',') # enter what you wil use to seperate the values
# if u want it to be space then leave the brackets blank

# above function will make the values into a list

tp = tuple(L)

print(L , tp)

# if you want it as a tuple you can do tuple(L) and it will return it as a tuple
# however it can only become a tuple from a list, not from a string
# so first it has to be a list then only a tuple

#! Dictionaries 

# Definition of dictionaries in Python with examples:
# A dictionary in Python is a collection of key-value pairs that are unordered, changeable, and indexed. Dictionaries are written using curly braces ({}) and each key-value pair is separated by a colon (:). The keys in a dictionary must be unique and immutable, while the values can be of any type and can be duplicated.

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'gender': 'male'}

# Accessing values in a dictionary
print(my_dict['name'])  # Output: John

# Adding a new key-value pair to a dictionary
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'gender': 'male', 'city': 'New York'}

# Removing a key-value pair from a dictionary
del my_dict['gender']
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, value)
# Output:
# name John
# age 30
# city New York

#! Lambda/Anon Functions:

x = lambda y:y+2 #this first y is the bound variable and the second is the body
#to use: 
print(x(10)) # will give 12

# or you can do it with more arguments:
z = lambda a,c:a*c
print(z(20,40))

# you can do:
# _(10,20) to use the most recent function

# you can also ask for input:

h = (lambda x, y, z: (x + y + z))(int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: ")))
print(h)

# and can also use multiple variables ^

i = (lambda *args:sum(args)) (int(input("Enter Number 1: ")), int(input("Enter Number 2: ")), int(input("Enter Number 3: ")))
print(i)

# or do this ^

#you can use the zip() function to print two lists combined:

l1 = ['blue' , 'red' , 'orange' , 'white']
l2 = ['sky' , 'apple' , 'sunset' , 'clouds']

fl = l1 + l2 
for i1,i2 in zip(l1,l2):
    print(i1,i2)


# Reading a file using open() function
file_path = "example.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# Writing to a file using open() function
new_content = "This is the new content of the file done using the open function."
try:
    with open(file_path, "w") as file:
        file.write(new_content)
        print("File updated successfully.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# you can use the zip function like this as well:

itemsds = [10, 20, 30, 40, 50]
numsds = [5, 10, 15, 20, 25]

zipped = [x + y for x, y in zip(itemsds, numsds)]

print(zipped)


#! Map, Zip, Filter, and Other Functions

# you can you map to map one list to other:

def sum(a,b):
    
    return a + b

items = [10, 20, 30, 40, 50]
nums = [5, 10, 15, 20, 25]

l = [x for x in map(sum,items, nums)]

print(l)

# and you can make more than just one function:

def multiply(a,b):

    return  a*b

n1 = [5,2,6]
n2 = [2,10,5]

multnumbs = [x for x in map(multiply,n1,n2)]

print(multnumbs)

# you can also use lambda for this:

L1 = [0,1,2]

for z in map(lambda x:x+10,L1):

    print(z)

# and it doesn't have to be 1 variable:

lis1 = [10,20,30]
lis2 = [5,10,15]

for w in map(lambda x,y:x+y,lis1,lis2):

    print(w)

# the filter funnction:
def isEven(a):

    if a % 2 == 0:

        return True 
    
    else:

        return False
    

LisT1 = [12,13,14,15,16,17,18]

filtr = [x for x in filter(isEven,LisT1)]
# returns only the true variables and instead of returning True,True,True, it returns the values (here the numbers)
print(filtr)

#how to add more paramaters while defining a function

def addNumbers(*numbrs):

    sum = 0

    for n in numbrs: 

        sum = sum + n

    print(sum)

addNumbers(10,20,30)

# this will allow for multiple numbers to be taken in

#! Classes
# In Python, classes are a fundamental concept of object-oriented programming (OOP)
# A class is like a blueprint or template for creating objects (instances)
# It defines a collection of attributes (variables) and methods (functions) that encapsulate the behavior and data associated with the objects

# Before showing you a class I have to show you how to construct one using a constructor called __init__
# The __init__ function is a special method in Python classes, also known as the constructor. It is automatically called when an instance of a class is created
# The purpose of the __init__ method is to initialize the attributes of an object to their initial values
# Here's how the __init__ method works in the context of our upcoming example of a class:

'''

def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.is_engine_on = False

'''

# In the upcoming example class, the __init__ method takes four parameters: self, make, model, and year. The self parameter is a reference to the instance being created
# Inside the __init__ method, we assign the values passed as arguments (make, model, year) to the instance variables (self.make, self.model, self.year)
# These variables hold the specific attribute values for each instance of the class
# Here's an example to illustrate the concept of classes in Python and the __init__ constructor:

class Airplane:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_engine_on = False

    def start_engine(self):
        self.is_engine_on = True
        print("Engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        print("Engine stopped.")

    def fly(self):
        if self.is_engine_on:
            print("Flying...")
        else:
            print("Please start the engine first.")

# Creating instances of the Airplane class
airplane1 = Airplane("Boeing", "747", 2000)
airplane2 = Airplane("Airbus", "A380", 2010)

# Accessing attributes
print(airplane1.make)  # Output: Boeing
print(airplane2.year)  # Output: 2010

# Calling methods
airplane1.start_engine()  # Output: Engine started.
airplane1.fly()  # Output: Flying...

airplane2.start_engine()  # Output: Engine started.
airplane2.fly()  # Output: Flying...

airplane1.stop_engine()  # Output: Engine stopped.
airplane1.fly()  # Output: Please start the engine first.

# For example, when we create the airplane1 instance with the statement airplane1 = Airplane("Boeing", "747", 2000)
# the __init__ method is automatically called with the provided arguments "Boeing", "747", and 2000
# It sets the make attribute of airplane1 to "Boeing", the model attribute to "747", the year attribute to 2000, and the is_engine_on attribute to False
# The __init__ method allows us to ensure that every instance of the class has its attributes properly initialized when created
# It provides a convenient place to set up the initial state of the object and perform any necessary setup or initialization tasks
# By defining the __init__ method, we can create objects with different initial attribute values by passing arguments during object creation, as demonstrated in the example

#Self:
# In Python, self is a conventional name used as the first parameter in a method definition within a class. It refers to the instance of the class itself
# When a method is called on an instance of a class, self is automatically passed as the first argument to that method
# The self parameter allows us to access the attributes and methods of the current instance within the class
# It acts as a reference to the specific object that the method is being called on
# By using self, we can access and modify the instance's attributes, call other methods within the class, or perform any operations specific to that instance
# For example, in our airplane class:

'''

def start_engine(self):
    self.is_engine_on = True
    print("Engine started.")

'''

# The start_engine method takes self as the first parameter. Inside the method, self.is_engine_on refers to the is_engine_on attribute of the current instance
# By using self, we can set the is_engine_on attribute of the current instance to True
# When we call the start_engine method on an instance, such as airplane1.start_engine(), the instance airplane1 is automatically passed as self
# Therefore, self within the method will refer to airplane1, and the is_engine_on attribute of airplane1 will be updated accordingly
# self is a reference to the instance of the class itself. It allows us to access and modify the instance's attributes and call other methods within the class
# Using self ensures that each instance can maintain its own unique state and behavior

#! Getters and Setters
# In object-oriented programming, getters and setters are methods used to access (get) and modify (set) the values of an object's attributes, respectively
# They provide a way to encapsulate the internal representation of an object and control access to its data
# Getters and setters are useful for maintaining data integrity and providing a level of abstraction between the object's internal representation and its usage by external code
# Here's an example of how getters and setters can be implemented in Python:

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        self._age = age

# Creating an instance of the Person class
person = Person("Alice", 25)

# Using the getter method to access the attribute
print(person.get_name())  # Output: Alice

# Using the setter method to modify the attribute
person.set_name("Bob")
print(person.get_name())  # Output: Bob

# Using the setter method with validation
person.set_age(30)
print(person.get_age())  # Output: 30

# In this example, the Person class has attributes _name and _age (prefixed with an underscore to indicate they are intended to be private)
# For each attribute, there is a getter method (e.g., get_name(), get_age()) and a setter method (e.g., set_name(), set_age())
# The getter methods simply return the values of the corresponding attributes
# The setter methods allow external code to modify the values but typically include additional logic to validate the input before updating the attribute
# By using getters and setters, we can control how attribute values are accessed and modified, ensuring consistency and enforcing any necessary constraints or transformations

#! Try and Expect 
# In Python, try and except are used together to implement exception handling
# It allows you to handle and recover from errors or exceptional situations that may occur during the execution of your code 
# So instead of the code stopping at an error it would be able to continue 
# The basic syntax of try and except is as follows:

'''

try:
    # Code that may raise an exception
    # ...
except ExceptionType:
    # Code to handle the exception
    # ...

'''

# If an exception is raised within the try block, the program flow is immediately transferred to the corresponding except block
# The ExceptionType in the except statement specifies the type of exception you want to catch and handle
# You can replace ExceptionType with a specific exception class, such as ValueError, TypeError, or use a more general Exception to catch any exception
# Here's an example that demonstrates the usage of try and except:

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero occurred.")

# In this example, we attempt to divide numerator by denominator, which is set to 0. Since division by zero is not allowed, a ZeroDivisionError exception is raised
# Using try and except allows you to anticipate and handle potential errors gracefully, preventing your program from crashing and/or providing alternative actions when exceptions occur

#! Creating a File using OS module

import os

file_path = "example.txt"

try:
    # Attempt to create a new file with mode "x" (exclusive creation)
    with open(file_path, "x") as file:
        print("File created successfully.")
except FileExistsError:
    # If the file already exists, handle the FileExistsError
    print("File already exists.")

# Writing to a File

file_path = "example.txt"

with open(file_path, "w") as file:
    # Open the file in write mode ("w") and use the write() method to add content
    file.write("Hello, this is some text.\n")
    file.write("This is another line of text.")

# Reading from a File

file_path = "example.txt"

with open(file_path, "r") as file:
    # Open the file in read mode ("r") and use the read() method to read the content
    content = file.read()
    print(content)

# Appending to a File

file_path = "example.txt"

with open(file_path, "a") as file:
    # Open the file in append mode ("a") and use the write() method to add content
    file.write("\nThis line will be appended to the file.")
