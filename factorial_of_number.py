# thi program prompt the user to enter the integer
# then calculate and display its factorial


number = int(input("input any positive integer : "))
factorial =1
if number < 0 :
    print("sorry the factorial of entered number is not valid")
elif number == 0:
    print("the factorial of ", number , " is 1")
else:
    for x in range(1,number+1) :
        factorial = factorial * x
    print("the factorial of ",number, 'is ',factorial)
