"""
# Polymorphism:
# OverRidding:

class A:
    def myfun(self):
        print("This is class A.")

class B(A):
    def myfun(self):
        super().myfun()
        print("This is class B.")

obj =B()
obj.myfun()
   """
"""
class G:
    def myfun(self):
        print("This is class G.")

class A:
    def myfun(self):
        super().myfun()
        print("This is class A.")

class B(A,G):
    def myfun(self):
        super().myfun()
        print("This is class B.")

obj =B()
obj.myfun()
"""
"""
def hello(fv):
    def fvx():
        print("Welcome to our website!!")
        fv()
        print("Thank you visit again !!")

    fvx()

@hello

def fac():
    n = int(input("Enter num : "))
    fac = 1
    for i in range(1,n+1):
        fac*=i
    print(fac)
"""
"""
class User:
    def get(self,__a,__b):
        self.__g = __a
        self.__h = __b

    def set(self):
        print("Value of A : ", self.__g)
        print("Value of B : ", self.__h)

obj = User()

obj.get(10,20)
obj.set()
"""

# Make a banking system :

class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)


s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
















