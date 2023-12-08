""" 1. Valid Number Information
Design a program that uses a loop to build a list named valid_numbers that contains only 
the numbers between 0 and 100 from the numbers list below. The program should then 
determine and display the total and average of the values in the valid_numbers list.
numbers = [74, 19, 105, 20, −2, 67, 77, 124, −45, 38] """

valid_number = []
average = 0
total = 0
j = 0

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
for i in range(len(numbers)):
    if numbers[i]> 0 and numbers[i]< 100:
        valid_number.append(numbers[i])

for i in range(len(valid_number)):
    
    total +=numbers[i]
    j =j+1
average = total/j
print('the total of list is : ', total)
print('the average is : ', average)
    


        