"""
s = input("Enter name : ")

l1 = int(len(s)/2)

if len(s)%2==0:
    print(s)

else:
    print(s[l1-1]+s[l1]+s[l1+1])

"""
"""

n = int(input("Enter number"))


for i in range(1,n+1):
    if i == 6:
        break           # break statement

    print(i)
"""
"""
n = int(input("Enter number"))

for i in range(1,n+1):
    if i == 6:
        continue                 # continue statement

    print(i)
"""

n = int(input("Enter number"))

for i in range(1,n+1):
    if i == 6:
        pass                 # continue statement

    print(i)
