"""2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, 
each in the range of 0 through 9, and assign each number to a 
list element. (Random numbers were discussed in Chapter 5.) Then write another loop that 
displays the contents of the list.
"""
import random
def lottery_number_gen():
    lottery_numbers = []
    for rand in range(7):
        j = random.randint(0,9)
        lottery_numbers.append(j)
    return lottery_numbers

def displaying_lottery_numbers(numbers):
    for number in numbers:
        print(number)

def main():
    lottery_numbers = lottery_number_gen()
    
    print('Generated Lottery Numbers:')
    displaying_lottery_numbers(lottery_numbers)
if __name__ == "__main__":  
    main()
