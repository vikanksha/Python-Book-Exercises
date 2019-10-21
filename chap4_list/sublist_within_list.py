# Write a Python program to check whether a list contains a sublist.
lst = [1,2,3,4,5,6,7,8]
s_lst = [9,1]
check = all(item in lst for item in s_lst)
if check is True:
    print('yes it cointain a sublist')
else:
    print('no its not')