# Write a Python program to insert a given string at the beginning of all items in a list.
lst = [12,13,14]
str = 'sweet'
l = []
for i in lst:
    l.append(str+'{0}'.format(i))
print(l)
