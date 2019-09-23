#Add all even no using while loop between 100 and 200.
max = 200
no = 100
sum = 0
while no <= max:
    if(no % 2 == 0):
        sum = sum + no
        no = no+1
print(sum)        