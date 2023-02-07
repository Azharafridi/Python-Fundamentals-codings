# this program get a word each time from user using loop
# and stop the loop by pressing the enter key
# at last will display the average length of the words

total_length = 0
word = 0
number_word = 0
average_length = 0


while word !="":
    word = input("Enter a word for running or enter key to stop the program : ")
    number_word +=1
    for characters in (word) :
        total_length += 1

average_length = total_length/number_word

print("the average length for words is : ", round(average_length))