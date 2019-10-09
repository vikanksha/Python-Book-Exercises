# Write a Python program to guess a number between 1 to 9.
import random
guess_no = 0
no_range = random.randint(1,10)
while no_range != guess_no:
    guess_no = int(input("Enter no between 1 to 10 untill you get it right : "))
print("Well guessed! ")