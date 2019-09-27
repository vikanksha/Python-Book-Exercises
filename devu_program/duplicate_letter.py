# Write a program to remove duplicate letters from a given word.
word = eval(input("Enter a word:"))
a = " "
for i in word:
    if i.lower() not in a.lower():
        a = a+i
print(a)        

