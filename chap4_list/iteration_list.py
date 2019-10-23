# Write a Python program to iterate over two lists simultaneously.
no = [1,2,3]
name = ['Ram', 'Shyam', 'Mohan']
for (a,b) in zip(no,name):
    print(a,b)