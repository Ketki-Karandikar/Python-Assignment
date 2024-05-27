# Inheritance
"""
# Single Level:
class A():
    def mul(self):
        a = int(input("Enter Number 1 : "))
        b = int(input("Enter Number 2 : "))
        print("Multiplication : ", a*b)

class B(A):
    def mul1(self):
        print("Multiplication completed !!")

OBJ = B()
OBJ.mul()
OBJ.mul1()

"""
"""
# Multi Level:
class G():
    def home(self):
        print("Multilevel programming !!")
class A(G):
    def mul(self):
        a = int(input("Enter Number 1 : "))
        b = int(input("Enter Number 2 : "))
        print("Multiplication : ", a*b)

class B(A):
    def mul1(self):
        print("Multiplication completed !!")

OBJ = B()
OBJ.home()
OBJ.mul()
OBJ.mul1()
"""
"""
# Multiple Level:
class A:
    def parent(self):
        print("This is Parent class!!")

class B:
    def subparent(self):
        print("This is subparent class!!")

class C(A,B):
    def child(self):
        print("This is child class!!")

obj = C()
obj.parent()
obj.subparent()
obj.child()
"""
"""
# Herarchi :
class A:
    def Child(self):
        print("This is Child class!!")

class B(A):
    def Mother(self):
        print("This is Mother class!!")

class C(A):
    def Father(self):
        print("This is Father class!!")

obj1 = B()
obj = C()
obj.Child()
obj.Father()
obj1.Mother()
obj1.Child()

"""
"""
# Hybrid :
class A:
    def Child(self):
        print("This is Child class!!")

class B(A):
    def Mother(self):
        print("This is Mother class!!")

class C():
    def Father(self):
        print("This is Father class!!")

class D(B,C):
    def Fish(self):
        print("This is Fish class!!")

obj = D()
obj.Child()
obj.Father()
obj.Mother()
obj.Fish()
"""

class batsman:
    def batsman(self):
        team_name = input("Enter name : ")
        team_score = input("Enter score : ")
        batsman_name = input("Enter batsman name : ")
        score_of_batsman = int(input("Enter score of batsman : "))
        n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        avg = sum(n)/len(n)
        print("team_score_avg : ", round(avg))        

class data(batsman):
    def data(self):
        name_of_bowler = input("Enter name of bowler : ")
        wickets = input("Numberv of wickets taken : ")
        name_of_man_of_the_match = input("Name of Man of the Match : ")
        print()
        
obj = data()
obj.batsman()
obj.data()





