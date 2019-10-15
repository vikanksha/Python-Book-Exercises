var = int(input("value :"))
size = 0
for i in range(var+1):
    if i%2 == 0:
        size = size+i
    else:
        size = size + i**2
print(size)