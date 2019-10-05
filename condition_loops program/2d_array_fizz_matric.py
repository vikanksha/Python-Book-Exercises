# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.also display sum of row and colum is even or not for even print fizz for odd print buzz. The element value in the i-th row and j-th column of the array should be i*j.
row_no = int(input("no of rows"))
col_no = int(input("no of col"))
#list = [[0 for col in range(row_no)]for row in range(col_no)]
list = []
for row in range(row_no):
    row_temp = []
    for col in range(col_no):
        if (row+col) % 2 == 0:
            col_temp = "Fizz"
        else:
            col_temp = "Buzz"
        row_temp.append(col_temp)
    #print(row_temp)
    list.append(row_temp)
print(list)        