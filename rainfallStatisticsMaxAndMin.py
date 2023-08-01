"""

3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a
list. The program should calculate and display the total rainfall for the year, the average
monthly rainfall, the months with the highest and lowest amounts.
"""

def main():
    rainFall = []
    total = 0.0
    average = 0.0
    maximum = None
    minimum = None

    # here the rainfall for each month is added

    print("enter the rainfall for each month consecutively")
    for count in range(12):
        monthlyRainFall = int(input("enter the rainfall : "))
        rainFall.append(monthlyRainFall)
        total +=monthlyRainFall

    # for printing the rainfall of each month
    for count in range(12):
        print(rainFall[count], end="  ")
    average = total / 12
    print("\nthe total rainfall is ", total, "\n", " the average rainfall is :", average)

    # finding the minimum
    for value in rainFall:
        if minimum is None:
            minimum = value
        elif value < minimum:
            minimum = value
    print("the minimum is : ", minimum)

    # finding the maximum
    for value in rainFall:
        if minimum is None:
            minimum = value
        elif value > minimum:
            minimum = value
    print("the minimum is : ", minimum)

main()