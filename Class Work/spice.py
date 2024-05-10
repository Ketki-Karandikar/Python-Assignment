
"""
def fun1():
    a = int(input("Enter num1"))
    b = int(input("Enter num2"))
    return (a+b)

print(fun1())

"""
"""
def prime():
    a = int(input("Enter num : "))
    c = 0
    for i in range(1,a+1):
        if(a%i==0):
            c+=1
    if c==2:
        return a, "is prime number."
    else:
        return a, "is not a prime number."
    
print(prime())
"""
"""
a = int(input("Enter num : "))

def prime(a):
    c = 0
    for i in range(1,a+1):
        if(a%i==0):
            c+=1
    if c==2:
        return a, "is prime number."
    else:
        return a, "is not a prime number."
    
print(prime(a))
"""

def sreverse():
    n = input("Enter string : ")

    print("Reverse string is : ", n[::-1])

def slen():
    n = input("Enter string : ")
    print("Length of the string is : ", len(n))

def smiddle():
    n = input("Enter string : ")

    n1 = int(len(n)/2)

    print("Middle of the string is : ", n[n1-1]+n[n1]+n[n1+1])

def smerge():
    n = input("Enter string 1 : ")
    n1 = input("Enter string 2 : ")

    print("Merge of string is", n+n1 )


sreverse()
slen()
smiddle()
smerge()


