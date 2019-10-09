# Write a Python program to check a triangle is equilateral, isosceles or scalene.
side1 = int(input("Enter a side of triangle:"))
side2 = int(input("Enter a side of triangle:"))
side3 = int(input("Enter a side of triangle:"))
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 != side2 != side3:
    print("scalene triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("isosceles triangle")
    