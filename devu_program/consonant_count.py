 # Write a program count the number of consonants in the word "Aeroplane"
word = "Aeroplane"
count = 0
for i in word:
    if i.lower() not in "aeiou":
        count = count+1
print(count)        