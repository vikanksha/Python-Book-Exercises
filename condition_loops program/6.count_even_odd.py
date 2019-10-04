# Write a Python program to count the number of even and odd numbers from a series of numbers.
no_list = [1,2,3,4,5,6,7,8,9,10,12,14,16]
even_count = 0
odd_count = 0
for i in no_list:
    if i % 2 == 0:
        even_count = even_count+1
    else:
        odd_count = odd_count+1
print("Even no :", even_count)
print("Odd no :" ,odd_count)