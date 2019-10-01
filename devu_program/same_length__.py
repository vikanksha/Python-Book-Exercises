# Write a program to print the given string along with underscores ‘_’ which is added to the same amount as the length of string.
word = eval(input("Enter a word :"))
print(word + '__' *len(word))