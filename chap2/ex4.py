# program for displaying result with eaxctly two decimals places.
first_integer = int(input("Enter first number"))
second_integer = int(input("Enter second number"))
result = float(first_integer//second_integer)
format(result,'.2f')