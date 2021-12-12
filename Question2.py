# importing the math library
# to be used to round up using math.ceil
import math

original_grade = [73,38,67,33]

# creating a function to take in the list of grades
# of the students
def gradingStudents(grade):
    # initializing a list where the rounded grades
    # will be stored
    final_grade = []
    
    # looping through the list 
    for grade in original_grade:
        # if the grade < 38, no need to round it
        # because it is a failing grade already
        if grade < 38:
            # adding the grade to our final_grade
            final_grade.append(grade) 
            
        else:
            # if the grade >= 38, 
            # find the nearest nearest multiple of 5 divide 
            # the grade by 5 and round the value to the 
            # nearest whole number using the math.ceil and 
            # mulitply by 5
            rounded_grade = math.ceil(grade/5)*5
            
            # if the difference between new_grade and grade is 
            # less than 3, then we can append the rounded grade final_grade array
            # else, we append the original grade to the final_grade array 
            if rounded_grade-grade < 3:
                final_grade.append(rounded_grade)
            else:
                final_grade.append(grade)
                
    # returning our rounded grades in the final_grade array 
    return final_grade

print("The original grades are: "+ str(original_grade))
print("The rounded  grades are: "+ str(gradingStudents(original_grade)))
