from spice import *

while True:

    menu = """

    press 1 For reverse the string
    press 2 For knowing th length of the string
    press 3 For knowing the middle of the string
    press 4 For Merging the String
    press 5 for exit



"""
    print(menu)
    print()
    
    choice = input("Enter your choice : ")
    if choice==1:
        a = int(input("Enter str 1 : "))
        b = int(input("Enter str 2 : "))
        print("sreverse : ")

    elif choice==2:
        a = input("Enter str 1 : ")
        b = input("Enter str 2 : ")
        print("slen : ")

    elif choice==3:
        a = input("Enter str 1 : ")
        b = input("Enter str 2 : ")
        print("smiddle : ")

    elif choice==4:
        a = input("Enter str 1 : ")
        b = input("Enter str 2 : ")
        print("smerge : ")

    elif choice==5:
        print("Thank you visit again")
        break

    else:
        print("Invalid choice")
        break
