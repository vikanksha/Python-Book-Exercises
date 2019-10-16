# Write a Python program to print the numbers of a specified list after removing even numbers from it.
lst = [1,2,3,4,5,9,8]
l = []
for i in lst:
    if i % 2 != 0:
        l.append(i)
print(l) 