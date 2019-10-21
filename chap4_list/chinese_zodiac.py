# chinese Zodiac program
zodiac_animals = ('rat','ox','tiger', 'rabbit','dragon','snake','horse','goat','monkey','rooster','dog','pig')
birth_yr = int(input("enter birth yr"))
cycle_num = (birth_yr-1900)%12
print(zodiac_animals[cycle_num])