# Write a Python program to check if all dictionaries in a list are empty or not.
my_list = [{},{}]
my_list1 = [{1,2},{}]
print(all(not i for i in my_list))
print(all(not i for i in my_list1))