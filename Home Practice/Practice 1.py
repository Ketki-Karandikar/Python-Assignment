"""
a = int(input("Enter your age : "))
print("Your age is : ", a)

# Conditional operators.

if(a>=18):
    print("You can drive.")
elif(a>60):
    print("Your age is invalid.")
else:
    print("You cannot drive.")
"""
"""
appleprice = 210
budget = 500
if (appleprice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
"""
"""
num = int(input("Enter num : "))
if(num<0):
    print("Number is negative")
elif(num > 10):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

"""

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)



