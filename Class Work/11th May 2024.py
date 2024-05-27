
"""
import math

n = int(input("Enter Number : "))
print(math.factorial(n))

"""
"""
file = open("test.txt", "w")
file.write("This is write method.")
file.close()
"""
"""
file = open("test_1.txt", "a")
file.write("This is append method.")
file.close()
"""
"""
file = open("test_1.txt", "r")
print(file.readlines())
file.close()
"""
"""
name = input("Enter your name : ")
mobile = int(input("Enter mobile number : "))
email = input("Enter email : ")
d[login] = str["d[name]=name"
        ,"d[mobile]=mobile"
        ,"d[email]=email"]


file = open("test_2.txt", "w")
file.write("d[name]=name, d[mobile]=mobile, d[email]=email")
file.close()
"""

"""
while True:
    menu = """
    # press 1 for login
    # press 2 for signup
    # press 3 to exit
    
"""
    choice = input("Enter your choice : ")
    if choice==1:
        name = input("Enter your name : ")
        mobile = int(input("Enter mobile number : "))
        email = input("Enter email : ")
        print("Succefully logged in!!")

    else:
        d[name]=name
        d[mobile]=mobile
        d[email]=email
        print("Invalid credentials!!")

    if choice==2:
        name = input("Enter your name : ")
        mobile = int(input("Enter mobile number : "))
        print("Succefully signed in!!")

    else:
        d[name]=name
        d[mobile]=mobile
        print("Invalid credentials!!")

    if choice==3:
        print("Thank you!!")
        break
    else:
        print("Invalid choice!!")
        break

"""

"""
file = open("test_4.txt", "w+")
file.write("This is w+ method.")

print(file.tell())
file.seek(0)
print(file.readline())
file.close()
"""
file = open("test_4.txt", "r+")
file.write("This is r+ method.")

print(file.tell())
file.seek(0)
print(file.readline())
file.close()


