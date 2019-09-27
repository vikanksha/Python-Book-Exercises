# Write a program to count the number of names beginning with vowels in a given tuple of names.
a = eval(input("Enter lists"))
count = 0
for i in a:
    if i[0].lower() in "aeiou":
        count = count+1
print(count)        
