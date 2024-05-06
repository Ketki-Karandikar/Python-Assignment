# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

# Taking input from the user
str_1 = input("Enter the string : ")
 
# to print the str_1
str_2 = "{}{}".format(str_1[0:2], str_1[-2:])
 
#Printing the str_2
print("str_1 = " + str_1)
print("str_2 = " + str_2)
