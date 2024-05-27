"""

# Abstraction Method

from abc import ABC,abstractmethod

class RBI(ABC):
    def roi(self):
        pass

class Kotak(RBI):
    def roi(self):
        print("Kotak rate is 8.10")

class SBI(RBI):
    def roi(self):
        print("SBI rate is 7.50")

class HDFC(RBI):
    def roi(self):
        print("HDFC rate is 7.68")


obj = Kotak()
obj.roi()

obj1 = SBI()
obj1.roi()

obj2 = HDFC()
obj2.roi()

"""

"""
from abc import ABC,abstractmethod

class Earthly(ABC):
    def salary(self):
        pass

class Ketki(Earthly):
    def salary(self):
        print("Ketki salary is 25000.")

class Alpha(Earthly):
    def salary(self):
        print("Alpha salary is 30,000.")

class Beta(Earthly):
    def salary(self):
        print("Beta salary is 20,000.")


obj = Ketki()
obj.salary()

obj1 = Alpha()
obj1.salary()

obj2 = Beta()
obj2.salary()

"""
"""

# lambda function:

x = lambda a,b,c: a*b*c

print(x(2,2,2))


# Filter

# Take a list of numbers. 
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ] 

# use anonymous function to filter and comparing 
# if divisible or not 
result = list(filter(lambda x: (x % 13 == 0), my_list)) 

# printing the result 
print(result) 

"""
"""
# Map()
# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(tuple(result))
"""


# Reduce()




