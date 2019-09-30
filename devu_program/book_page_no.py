# WAP to find the number of occurances of digit in book page numbers.
pages = int(input("Book Size :"))
page_digit = (input("Page Digit :"))
print(" ".join ([str(i)for i in range(1,pages+1)]).count(page_digit))

