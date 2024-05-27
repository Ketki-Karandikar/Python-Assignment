# try and error
"""
try:
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))

    print("Addition : ", n1+n2)

except ValueError as e:
    print(e)

else:
    print("Try excetured!!")

finally:
    print("Finally Executed !!")

"""
"""


try:
    l = [1, 2, 3, 4, 5]

    n = int(input("Enter number : "))

    print("Value is : ", l[n])

except:
    print("Invalid Input")
"""
"""
class Myclass():
    def add(self):
        n = int(input("Enter number : "))
        n1 = int(input("Enter number 1 : "))
        print("Addition : ", n+n1)

    def fac(self):
        n = int(input("Enter number : "))
        print("Factorial : ", n)

    def mul(self):
        n = int(input("Enter number : "))
        n1 = int(input("Enter number 1 : "))
        print("Multiplication : ", n*n1)

obj = Myclass()
obj.add()
obj.fac()
obj.mul()
"""

"""
class Myclass():
    def add():
        n = int(input("Enter number : "))
        n1 = int(input("Enter number 1 : "))
        print("Addition : ", n+n1)

    def fac():
        n = int(input("Enter number : "))
        print("Factorial : ", n)

    def mul():
        n = int(input("Enter number : "))
        n1 = int(input("Enter number 1 : "))
        print("Multiplication : ", n*n1)

obj = Myclass
obj.add()
obj.fac()
obj.mul()
"""

class Myclass():
    def add():
        n = int(input("Enter number : "))
        n1 = int(input("Enter number 1 : "))
        print("Addition : ", n+n1)

    class Myclass2():
    
        def fac():
            n = int(input("Enter number : "))
            print("Factorial : ", n)

class Myclass3():

    def mul():
        n = int(input("Enter number : "))
        n1 = int(input("Enter number 1 : "))
        print("Multiplication : ", n*n1)

obj = Myclass
obj.add()
obj2 = obj.Myclass2
obj2.fac()
obj3 = Myclass3
obj3.mul()









