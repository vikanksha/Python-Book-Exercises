# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
lst = ['abc', 'xyz', 'aba', '1221']
count = 0
for w in lst:
    if w[0] == w[-1]:
        count = count+1
print(count)