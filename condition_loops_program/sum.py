# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
no1 = int(input("Enter no:"))
no2 = int(input("Enter no:"))
sum = no1+no2
if sum in range(15,20):
     print(20)
else:    
    print(sum)