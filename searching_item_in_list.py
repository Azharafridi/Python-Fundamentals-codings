# this program search the index number for an item in list

def main():
    # creating a list
    products = ['A955', 'Q789', 'R222']

    # searching for an item
    search = input('enter the index number in the array to search :\n')
    if search in products:
        print(search, 'found in the list ')
    else:
        print(search,'does not found')

main()