 #! Basic's and aritmetic operations
# str(value) turns it into a string, meaning a text (can also be called objects)
# int(value) make it into a number
# float(value) into a decimil number
# bool(value) into a boolean which is a true or false
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
    # you can see that neat little += 1 instead of i = i + 1 coming in handy there 
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

func("Haris", "The Human") # here you enter the values of the variables 

