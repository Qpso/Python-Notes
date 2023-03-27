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