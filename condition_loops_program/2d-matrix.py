# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
row_no = 2
col_no = 2 
# for row in range(row_no):
#     print(row)
#     for col in range(col_no):
#         list[row][col] = 0  
# print(list)       
list = []
for row in range(row_no):
    row_temp = []
    for col in range(col_no):
        if (row+col) % 2 == 0:
            col_temp = "fiz"
        else:
            col_temp = "buzz"
        row_temp.append(col_temp)
    print(row_temp)    
    list.append(row_temp)        
print(list)   