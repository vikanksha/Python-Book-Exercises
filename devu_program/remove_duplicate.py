# WAP to find the uncommon data items in two given lists. Also sort the result and remove duplicates if any.
list1 = eval(input("Enter first list"))
list2 = eval(input("Enter second list"))
uncommon_list = []
for m in list1:
    if m not in list2:
        if m not in uncommon_list:
            uncommon_list.append(m)
for n in list2:
    if n not in list1:
        if n not in uncommon_list:
            uncommon_list.append(n)
print(uncommon_list)            