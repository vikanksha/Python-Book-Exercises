# WAP to sum of first digits in a given list of number.
list_number = eval(input("Enter list :"))
sum = 0
for i in list_number:
    sum = sum + int(str(i)[0])
print(sum)    
    