"""
x = int(input("Enter the value of x : "))
# x is the variable to match
match x:
    # if x is a 0
    case 0:
        print("x is zero")
        # case with if-condition
    case 4 if x %2==0:
        print("x %2==0 and case is 4")
        # Empty case with if-condition
    case _ if x<10:
        print("x is < 10")

    # default case (will only be matched if the above  cases were not matched)
    # So it is basically just an else:
    case _:
        print(x)
        """
"""
name = "Ketki"
for i in name:
    print(i)

    """
"""
colors = ["Red", "Green" "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
"""
    
"""
for k in range(5):
    print(k)
"""
"""
for k in range(1,9,2):
    print(k)
    """
"""
count = 5
while(count > 0):
    print(count)
    count = count - 1
"""
"""
x = int(input("Enter number : "))
while (x>0):
    print(x)
    x = x-1

else:
    print("Counter is 0")
"""







