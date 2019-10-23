# chinese Zodiac program
zodiac_animals = ('rat','ox','tiger', 'rabbit','dragon','snake','horse','goat','monkey','rooster','dog','pig')
terminate = False
while not terminate:
    
    birth_yr = int(input("enter birth yr"))
    cycle_num = (birth_yr-1900)%12
    print(zodiac_animals[cycle_num])
    response = input('would you like to enter another year ? (y/n):')
    while response != 'y' and response != 'n':
        response = input("please enter 'y' or 'n':")
    if response == 'n':
        terminate = True