# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
list = []
for i in range(100,401):
    i = str(i)
    if (int(i[0]) % 2 == 0) and (int(i[1]) % 2 == 0) and (int(i[2]) % 2 == 0):
        list.append(i)
print(list)        