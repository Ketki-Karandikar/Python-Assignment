"""
# tuple

t = (1, 2, "Ketki", 1.2, 3.5)

l = list(t)

print(l)

l.append(100)
print(l)
"""

"""
d = {1:"Ketki", 2:"Karan"}

print(d.get(1))  # To get that particular value of key
print(d.items())

d.update({3:"Ketki", 5:"Sky"})  # To update the dictionary
print(d)
d.pop(5)  # to delete the key or value
print(d)

t = {1,2,3}
d1 = d.fromkeys(t,6)   # to get the keys from set
print(d1)
"""

"""
d = {1:"Ketki", 2:"Karan"}  # To print the default key or value
print(d.setdefault(1))

"""

""""
d = {}

for i in range(1,31):
    d[i] = i*i

print(d)
"""

"""
d = {}

s = input("Enter String : ")

for i in s:
    if i in d:
        d[i]+=1

    else:
        d[i] = 1
        
print(d)
"""

l = [1, 2, 3]
l1 = [6, 7, 8]

print("Original Key is : ", +int(input(l)))
print("Original Value is : ", +int(input(l1)))

d = {}

for i in l:
    for j in l1:
        d[i]=j
        l1.remove(j)
        break

print(d)
print(l)
print(l1)

