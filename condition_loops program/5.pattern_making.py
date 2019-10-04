n = 5;
for i in range(0,n):
    for j in range((n-i)*5):
        print("*", end=" ")
    print('')  
for i in range(2,n+1):
    for j in range(i*5):
        print("*" , end = " ")
    print('') 