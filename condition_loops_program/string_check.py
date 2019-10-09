# Write a Python program to check a string represent an integer or not.
string = input("input a string:")
if all(string[i] in '0123456789'for i in range(len(string))):
    print("string is integer")
else:
    print("string is not integer")