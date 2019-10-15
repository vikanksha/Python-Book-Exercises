# Write a Python program to find the list of words that are longer than n from a given list of words.
def lst_length(n,lst):
    for i in lst:
        if len(i) > n:
            print(i)
lst_length(3,['sweet', 'ram', 'suchi', 'poem','kick']) 