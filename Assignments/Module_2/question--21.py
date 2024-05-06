# Write a Python function to reverse a string if its length is a multiple of 4.


def sreverse():
    str = input("Enter string : ")
    if len(str)%4==0:
        print("Reverse string is : ", str[::-1])
    else:
        print(str)

sreverse()
