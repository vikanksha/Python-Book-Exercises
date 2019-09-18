# temp conversion
choice = eval(input("Enter selection"))
while choice !="F" and choice != "C":
    temp = int(input("enter temp to convert"))
if choice == "F":
    converted_temp = (temp-32)*5/9
    print(temp , "degree fahrenheit is equal to" , converted_temp, "degree celcius")
else:
    converted_temp = (9/5*temp)+32
    print(temp , "degree celcius is equal to" , converted_temp, "degree fahrenheit")