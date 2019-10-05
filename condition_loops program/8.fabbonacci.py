# Write a Python program to get the Fibonacci series between 0 to 50.
def fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < 50:
        print(a , end = " ")
        c = a+b
        a = b
        b = c
        i = i + 1
fibonacci(50)        