# Write a Python program to remove duplicates from a list.
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    print(final_list)
remove([20,10,20,30,40,50])