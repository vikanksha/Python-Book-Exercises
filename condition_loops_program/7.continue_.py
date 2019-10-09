# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
no = [0,1,2,3,4,5,6]
for i in no:
    if i % 3 == 0:
        continue
    print(i , end = " ")  