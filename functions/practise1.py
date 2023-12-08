def make_shirt(size, text):
    if size >= 20:
        print('i love python')
    else:
        print('i dont love python')
    # print('the size is : ', size, ' ', text)
    
make_shirt(19,'')

# calling the function using keyword arguments

make_shirt(size = 26, text='armour under')