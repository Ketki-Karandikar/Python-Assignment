
"""

List
l = [1, 1.3256485, "Ketki", 1, 1, "Elephant"]

l.append(95)
print(l)
l.extend([45])
print(l)
l.pop(1)
print(l)
l.extend("Light")
print(l)
l.index("Ketki")
print(l)
l.reverse()
print(l)
l1 = [5, 4, 2, 1, 3]
l1.sort()
print(l1)
"""
"""
l = []
ev = []
od = []

for i in range(1,31):
    l.append(i)
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)
print(l)
print(ev)
print(od)
"""
"""
l = [1, 65, 23, 98, 10, 54]

l.sort()
print(l)

print("First Element : ", l[0])
print("Last Element : ", l[-1])
print("Last Second Element : ", l[-2])
"""

l = [1, 65, 23, 98, 10, 54]
l1 = []
l2 = []
for i in l:
    if i not in l1:
        l1.append(i)
        
    else:
        l2.append(i)

print(l1)
print(l2)