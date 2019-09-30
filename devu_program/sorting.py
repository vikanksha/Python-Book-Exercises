# WAP to find the uncommon data items in two given lists. Also sort the result and remove duplicates if any.
list1 = eval(input("Enter list1"))
list2 = eval(input("Enter list2"))
uncommon = []
for m in list1:
    if m == list2:
        break
    uncommon.append(m)
print(uncommon)    