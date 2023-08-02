"""
this program ask the user to enter the number of students in a class. Then it will itself generate their mid, final and will total 
each student marks. Then it will find the lowest and highest student marks
After that it will group the students according to their marks obtained such that from 0 to 10 , 11 to 20 and so on.
And on the basis of this list of students it produce the last result through graph. One steric for each student.
"""

import random



def main():
    mid_marks = []
    final_marks = []
    total_marks = []
    frequency = [0,0,0,0,0,0,0,0,0,0]
    No_students = int(input("Please enter the number of students : "))
    
    print("below are the mid marks : ")

    # here is the loop for the mid marks
    for i in range(No_students):
        marks = random.randint(0,30)
        mid_marks.append(marks)
    print(mid_marks)
    
    print("below are the final exam marks :")
    # this loop is for final marks
    for i in range(No_students):
        marks = random.randint(0,70)
        final_marks.append(marks)
    print(final_marks)
    
    # initialize the total marks with zero
    total_marks = [0] * No_students
    # finding total marks for each student
    for i in range(No_students):
        total_marks[i] = mid_marks[i] + final_marks[i]
    
    print("the total marks are : ")
    print(total_marks) 
    
    # finding highest and lowest students marks in total marks
    maximum_element = total_marks[0]
    
    for element in range(No_students):
        if total_marks[element] > maximum_element:
            maximum_element = total_marks[element]
    print("the highest marks is ", maximum_element)

    # finding the minimum marks in total marks

    minimum_element = total_marks[0]
    
    for element in range(No_students):
        if total_marks[element] < minimum_element:
            minimum_element = total_marks[element]
    print("the lowest marks is ", minimum_element)
    
    # now printing the total result through stars such that it shows result in groups as from 0 to 10 , 11 to 20 , 21 to 30 and so on
    # so making a new list for grouping so we called it as frequency
    
    for i in range(No_students):
        if total_marks[i] >= 0 and total_marks[i] <= 10:
            frequency[0] =+1 
        elif total_marks[i] >= 11  and total_marks[i] <= 20:
                frequency[1] =+1 
        elif total_marks[i] >= 21  and total_marks[i] <= 30:
                frequency[2] =+1  
        elif total_marks[i] >= 31  and total_marks[i] <= 40:
                frequency[3] =+1 
        elif total_marks[i] >= 41  and total_marks[i] <= 50:
                frequency[4] =+1 
        elif total_marks[i] >= 51  and total_marks[i] <= 60:
                frequency[5] =+1 
        elif total_marks[i] >= 61  and total_marks[i] <= 70:
                frequency[6] =+1 
        elif total_marks[i] >= 71  and total_marks[i] <= 80:
                frequency[7] =+1 
        elif total_marks[i] >= 81  and total_marks[i] <= 90:
                frequency[8] =+1 
        elif total_marks[i] >= 91  and total_marks[i] <= 100: 
                frequency[9] =+1   
    print(frequency)    
    
    print("now printing the above frequency list in the graph form :")
    
    for i in range(10):
        if frequency[i] > 0:
            for j in range(frequency[i]):
                print("*")
        else:
            print("") # empty line for no value in this range
        
            
    
            
    
main()