largest = None
smallest = None
count = 0
total = 0
while True:
    try:

        number = input("Enter a number: ")
        if number == "done":
            break
        number = int(number)
        count += 1
        total = number + total
        if largest == None and smallest == None:
            largest = number
            smallest = number
        if largest == None or number > largest:
            largest = number
        if smallest == None or number < smallest:
            smallest = number
    except:
        print("Invalid input")
print("The maximum number is: {}".format(largest))
print("The minimum number is: {}".format(smallest))
# print("The total number is: {}".format(total))
# print("The count number is: {}".format(count))