# Write a Python program to find the list in a list of lists whose sum of elements is the highest.
lst = [[1,2,3],[4,5,6],[7,8,9]]
l = []
for sub_lst in lst:
    sum = 0
    for element in sub_lst:
        sum = sum+element
    l.append(sum)
max_val = l[0]
for element in l:
    if element > max_val:
        max_val = element
print(lst[l.index(max_val)]) 