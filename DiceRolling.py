"""

6. Dice Rolling Function
In a program, write a function named roll that accepts an integer argument number_
of_throws. The function should generate and return a sorted list of number_of_throws
random numbers between 1 and 6. The program should prompt the user to enter a positive
integer that is sent to the function, and then print the returned list

"""
import random

def roll(number_of_throws):
    numbers = []
    for count in range(number_of_throws):
        numbers.append(random.randint(1, 6))
    print(numbers)

def main():
   number = int(input("enter any positive integer : "))
   if number < 0 :
       print("invalid number please enter the positive number ")
   else:
        print("here are the numbers of list printed")
        roll(number)
main()




