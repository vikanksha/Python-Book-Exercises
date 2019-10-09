# Write a Python program that accepts a word from the user and reverse it.
word = eval(input("Enter a word to reverse :"))
for char in range(len(word) -1,-1,-1):
    print(word[char], end = "")
print("\n")    