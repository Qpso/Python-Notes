# here's an example of a function using stuff we've learnt so far: 
# function to find average marks 
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks


# calculate grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade 

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print("Your average marks are", average_marks)


grade = compute_grade(average_marks)
print("Your grade is", grade)

# here's another example:
def multiply(*numbers):
    total = 1 
    for number in numbers:
        total *= number
    return total 

#! Example Using For Loops and If statements to make a prime number calcualtor:
num = int(input("Input a number: "))

if num>1:

    for i in range(1,num):


        if num == 2:
            print("2 is a prime number")
            break
        

        elif num%i == 0:
            print(num , "is not a prime number")
            break



        else:
            print(num , "is a prime number")
            break

else:
    print("Enter a number higher tha 1")
    

#? Basic Function Example: 
def add(num1, num2): # num1 and num2 are called parameters 
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is", result)

add(3, 5)
            

