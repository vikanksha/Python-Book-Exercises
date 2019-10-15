# 4. write a definition of a method COUNTDOWN(PLACES) to find and display those place names, in which there are more than 5 characters.
# ['DELHI', 'LONDON', 'PARIS', 'NEW YORK', 'DUBAI']
def countdown(places):
    for p in places:
        if len(p) > 5:
            print(p)
print(countdown(['DELHI', 'LONDON', 'PARIS', 'NEW YORK', 'DUBAI']))