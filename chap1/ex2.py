#Count no of days in a month
month = int(input("Enter the month(from 1-12) :"))
if month==2:
    year = int(input("please enter the year :"))
    if (year%4==0 and (not(year%100==0)or (year%400==0))):
        num_of_days = 29
    else:
        num_of_days = 28
elif month in (1,3,5,7,8,10,12):
        num_of_days = 31
elif month in (4,6,9,11):
        num_of_days = 30
else:
        print("Invalid Value entered , Please enter valid month")
print("There are", num_of_days, "Days in the month") 