# Write a Python program to get the largest number from a list.
lst = [-2,4,6,8,10]
max = 1
for i in lst:
    if i < max:
        max = i
print(max)        