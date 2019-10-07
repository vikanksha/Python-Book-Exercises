# Write a Python program that accepts a string and calculate the number of digits and letters.
string = eval(input("Enter a word mix of letter and digit :"))
dcount = 0
alphacount = 0
for i in string:
    if i.isdigit():
        dcount = dcount+1
    if i.isalpha():
        alphacount = alphacount+1
print("no of digits :" , dcount , "no of letters :" , alphacount) 