#  Write a program to print a list of numbers from 1to 50, replace every 3divisible number with “Fizz”, every 5 divisible number with “Buzz” and both 3 and 5 divisible numbers with “FizzBuzz”.
def list_no(n):
    l = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            l.append('FizzBuzz')
        elif i % 3 == 0:
            l.append('fizz')
        elif i % 5 == 0:
            l.append('Buzz')
        else:
            l.append(i)
    return l       
print(list_no(50)) 