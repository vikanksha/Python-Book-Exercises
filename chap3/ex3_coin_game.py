import random
print("The purpose of this exercise is to enter a no of coin values\n that add up to a displayed target value")
print("Enter coins value as 1-penny, 5-nickle, 10-dim, and 25 quarter")
print("Hit run after the last entered coin value")
print("-----------------")
terminate = False
empty_str = ''
while not terminate:
    amount = random.randint(1,99)
    print("Enter coins that add up to", amount, "cents, one per line.\n" )
    game_over = False
    total = 0
    while not game_over:
        valid_entry = False
        while not valid_entry:
            if total == 0:
                entry = input('enter first coin:')
            else:
                entry = input('enter next coin:')
            if entry in (empty_str,'1','5','10','25'):
                valid_entry = True
            else:
                print('Invalid entry')
        if entry == empty_str:
            if total == amount:
                print('correct!')
            else:
                print('sorry- you only entered', total, 'cents.')
            game_over = True
        else:
            total = total + int(entry)
            if total>amount:
                print('sorry - total amount exceeds', amount, 'cents')
                game_over = True
        if game_over:
            entry = input('\nTry again (y/n)? :')
            if entry == 'n':
                terminate = True
print('Thanks for playing........goodbye')