# Write a Python program to find common items from two lists. 
lst1 = [1,2,3,4,6,7]
lst2 = [6,7,8,9,10,11]
common_lst = []
for i in lst1:
    if i in lst2:
        common_lst.append(i)
print(common_lst)   