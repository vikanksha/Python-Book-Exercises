# Write a Python program to create the multiplication table (from 1 to 10) of a number.
no = int(input("Enter a no for table:"))
for i in range(1,11):
    print(no ,'x', i ,'=', no*i)