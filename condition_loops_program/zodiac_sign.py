# Write a Python program to display astrological sign for given date of birth.
date = int(input("Enter your birthdate:"))
month = input("Enter your birthmonth:")
if month == "Jan" and date >= 20 or month == "Feb" and date <= 18:
    print('Aquarius')
elif month == "Feb" and date >=19 or month == "Mar" and date <= 20:
    print('Pisces')
elif month == "Mar" and date >= 21 or month == "April" and date <= 19:
    print('Aries')
elif month == "April" and date >= 20 or month == "May" and date <= 20:
    print('Taurus')
elif month == "May" and date >= 21 or month == "June" and date <= 21:
    print('Gemini')
elif month == "June" and date >= 22 or month == "July" and date <= 22:
    print('Cancer')
elif month == "July" and date >= 23 or month == "Aug" and date <= 22:
    print('Leo')
elif month == "Aug" and date >= 23 or month == "Sep" and date <= 22:
    print("Virgo")
elif month == "Sep" and date >= 23 or month == "Oct" and date <= 23: 
    print('Libra')
elif month == "Oct" and date >= 24 or month == "Nov" and date <= 21:
    print('Scorpio')
elif month == "Nov" and date >= 22 or month == "Dec" and date <= 21:
    print('Saggitarius')
elif month == "Dec" and date >= 22 or month == "Jan" and date <= 19:
    print('Capricon')