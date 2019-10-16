# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
n = []
for i in enumerate(lst):
    if i[0] not in (0,4,5):
        n.append(i)
print(n)

