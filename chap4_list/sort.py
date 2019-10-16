# Write a Python function that takes two lists and returns True if they have at least one common member.
def common_lst(lst1,lst2):
    
    result = False
    for i in lst1:
        for j in lst2:
            if i == j:
                result = True
                return result
print(common_lst(['sweet', 'pooja','ruchi','prity', 'rani'],['sweety', 'pria','ruchi','prity', 'ravi']))