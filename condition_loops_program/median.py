# Write a Python program to find the median of three values.
val1 = int(input('Enter value 1:'))
val2 = int(input('Enter value 2:'))
val3 = int(input('Enter value 3:'))
if val1 < val2 and val2 < val3:
    print('median is', val2)