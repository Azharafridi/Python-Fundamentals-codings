"""

4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list then display the following data:
•	 The lowest number in the list
•	 The highest number in the list
•	 The total of the numbers in the list
•	 The average of the numbers in the list
"""

def main():
    total = 0.0
    average = 0.0

    numbers = []
    # taking the series of 20 numbers
    print("enter the 20 numbers in series ")
    for count in range(20):
        number = int(input("enter the number :  "))
        numbers.append(number)
        total += number

    # finding the minimum
    for value in numbers:
        if minimum is None:
            minimum = value
        elif value < minimum:
            minimum = value
    print("the minimum is : ", minimum)

    # finding the maximum
    for value in numbers:
        if minimum is None:
            minimum = value
        elif value > minimum:
            minimum = value
    print("the minimum is : ", minimum)

    average = total / 20
    print("total is : ", total)
    print("the average is : ", average)
