#  this program take input from the user and then write in the file


def main():
    #  taking input
    print('enter your three friends name ')
    name1 = input('name 1 : ')
    name2 = input('name 2 : ')
    name3 = input('name 3 : ')
    my_file = open('my_friends_name', 'w')
    # writing above inputs to the files
    my_file.write(name1 + '\n')
    my_file.write(name2 + '\n')
    my_file.write(name3 + '\n')

    my_file.close()
    print('the names are written successfully ')

main()