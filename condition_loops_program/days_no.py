# Write a Python program to convert month name to a number of days.
print("list of month : January, February, March, April, May, June, July, August, September, October, November, December")
Month = input("Enter month name :")
if Month == "Februrary":
    print("no of days 28/29")
elif Month in ("January" , "March", "May", "July", "August", "November" , "December"):
    print("no of days 31")
elif Month in ("April","June", "September" , "October"):
    print("no of days 30")
else:
    print("wrong month") 