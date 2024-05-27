# Make a lottery game in which the 

import random
l1 = random.randint(1,51)

l = ()

d = input("Enter the number : ")

for i in range(1,51):
    if i==l and l==l1:
        print("Congratulations you Won the Lottery!!")
    elif i>1:
        print("Enter the number greater than 1")
    elif i<51:
        print("Enter the number less than 51")
    else:
        print("Better Luck Next Time!!")

    