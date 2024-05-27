"""
n = int (input ("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i
print("Factorial of the given number is: ", factorial)

def add(a,b):           # add

    print("Addition : ", a+b)

def sub(a,b):        # substraction

    print("Substraction : ", a-b)

def mul(a,b):          # multiplication

    print("Multiplication : ", a*b)

def div(a,b):       # division

    print("Division : ", a/b)

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))        # division


add(a,b)
sub(a,b)         # to access or call the function
mul(a,b)
div(a,b)
factorial(a)
"""

while True:
    menu = """
    
    press 1 for Addition :
    press 2 for substraction :
    press 3 for multiplication :
    press 4 for division :
    press 5 for exit :



"""
    print(menu)
    print()

    choice = int(input("PLEASE ENTER YOUR CHOCIE = "))
    if choice==1:
        a = int(input("Enter number 1 : "))
        b = int(input("Enter number 2 : "))
        print("Addition : ", a+b)

    elif choice==2:
        a = int(input("Enter number 1 : "))
        b = int(input("Enter number 2 : "))
        print("Substraction : ", a-b)

    elif choice==3:
        a = int(input("Enter number 1 : "))
        b = int(input("Enter number 2 : "))
        print("Multiplication : ", a*b)

    elif choice==4:
        a = int(input("Enter number 1 : "))
        b = int(input("Enter number 2 : "))
        print("division : ", a/b)

    elif choice==5:
        print("Thank you visit again")
        break

    else:
        print("Invalid choice")
        break
