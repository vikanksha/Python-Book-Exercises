# Write a Python program to find all the values in a list are greater than a specified number.
lst = [12,10,15,19,25,9,17,7]
l = []
for i in lst:
    if i > 15:
        l.append(i)
print(l)    