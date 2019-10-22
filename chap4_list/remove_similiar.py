# Write a Python program to remove duplicates from a list of lists.
lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l = []
for element in lst:
    if element not in l:
        l.append(element)
print(l) 