# Write a program to return a list of all the names before a specified name.
list_of_names = eval(input(" "))
speci_name = input(" ")
list = []
for i in list_of_names:
    if i == speci_name:
        break
        list_of_names.append(i)
print(list)