# Write a program to delete first and last values from a list of any length.
def delete_first_last(a):
    if len(a)==0:
        return []
    elif len(a)==1:
        a.pop()
        return a
    else:
        a.pop(0)
        a.pop()
        return a
print(delete_first_last([1, 2, 3, 4])) 
