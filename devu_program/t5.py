#5. Write a program to reverse a dictionary consider both duplicate and non-duplicate values scenario.
a = {'a':101, 'b':201, 'c':301, 'd':101}
new_a = {}
for key, value in a.items(): 
    if value not in new_a: 
        new_a[value] = [key] 
    else: 
        new_a[value].append(key) 
print((new_a))

