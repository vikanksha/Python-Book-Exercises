# 3 .consider the randomly ordered numbers in the following list. filter numbers greater than 250 and return them in ascending order.
# [786,234,526,132,345,467]

lst = [786,234,526,132,345,467]
l = []
for i in lst:
    if i > 250:
        l.append(i)
        l.sort()
print(l) 