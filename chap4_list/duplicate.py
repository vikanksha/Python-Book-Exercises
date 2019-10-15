# Write a Python program to remove duplicates from a list.
lst = [(2, 1), (1, 2), (4, 4), (2, 3), (2, 1)]
l = []
for i in lst:
    if i not in l:
        l.append(i)
print(l)   