# Write a Python program to count the occurrences of each word in a given sentence ?

word = "Orange"     
count = 0
with open("temp.txt", 'r') as a:    # sample text file opening
	for line in a: 
		words = line.split() 
		for i in words: 
			if(i==word): 
				count=count+1
print("Occurrences of the word", word, ":", count)
