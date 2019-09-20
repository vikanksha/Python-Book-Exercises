# program for calculating a persons approx age in second.
import datetime
birth_month = int(input("Enter your birth month(1-12):"))
birth_day = int(input("Enter your birth date(1-31):"))
birth_year = int(input("Enter your birth year(4 digit):"))

current_month = int(input("Enter current month"))
current_date = int(input("Enter current date"))
current_year = int(input("Enter current year"))

no_of_sec_day = 24*60*60
no_of_sec_year = 365*no_of_sec_day

avg_no_sec_year = 4*(no_of_sec_year + no_of_sec_day)//4
avg_no_sec_month = avg_no_sec_year //12

no_sec_1900_dob = (birth_year-1900 * avg_no_sec_year) + (birth_month - 1 * avg_no_sec_month) + (birth_day * no_of_sec_day)
no_sec_1900_today = (current_year-1900 * avg_no_sec_year) +  (current_month - 1 * avg_no_sec_month) + (current_date * no_of_sec_day)
age_in_sec = no_sec_1900_today - no_sec_1900_dob
print('you are approx',age_in_sec, 'seconds old')