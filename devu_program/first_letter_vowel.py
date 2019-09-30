# Write a program to count the number of names beginning with vowels in a given tuple of names.
word_list = eval(input("Enter word list:"))
count = 0
for l in word_list:
    if l[0].lower() in 'aeiou':
      count = count+1
print(count)        