#program for first time home buyer tax credits.
# credit was only available to those who fullfill all criteria.
house_cost = int(input("Enter total your total house cost:"))
combine_income = int(input("Enter your total combine income:"))
previous_house = eval(input("Any house owened in last 3 years ? "))
if (house_cost < 800000) and (combine_income < 225000) and previous_house =='No'.lower():
    print("Congtrats !! you are eligible for first time home buyer tax credits of $8,000")
else:
    print('you are not eligible for credits amount')