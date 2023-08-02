"""

2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should
 generate seven random numbers, each in the range of 0 through 9, and assign each number to a
list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
displays the contents of the list
"""

import random

def main():
    # here is the empty list to store the numbers
    numbers = []
    # here the 7 random numbers are generated
    for count in range(7):
        numbers.append(random.randint(0, 9))    # here 0 and 9 shows the range at which the numbers will generate

    # here is the printing of the these numbers occured
    for index in range(7):
        print(numbers[index], end="")

main()