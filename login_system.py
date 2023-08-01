# this program uses the first three characters of the first and last name
# and the last three integers of the id and generate a passward for the user

def get_login_name(first, last, idnumber):
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = idnumber[-3:]
    login_name = set1 + set2 + set3
    return login_name


def main():
    print("enter your data : ")
    first = input("Enter your first name : ")
    last = input("enter your last name : ")
    idnumber = input("enter your id number : ")

    print("your log in password is : ")
    print(get_login_name(first, last, idnumber))

main()