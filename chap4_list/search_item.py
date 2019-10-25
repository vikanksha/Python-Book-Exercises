# search item in a list.
lst = [1,2,3,4,5]
search_item = 5
found = False
for item in lst:
    if item == search_item:
        found = True
        break
if found:
    print('found')
else:
    print("not found")