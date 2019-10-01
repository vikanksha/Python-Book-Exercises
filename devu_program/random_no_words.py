import random
no_range = (0,10)
#return random.randrange(no_range)
words_list = ['Ram','Shyam','lucky','Puja','Kabir','Rani','Neha','Sonu','Monu','Raju']
game_no = random.randrange(0,10,1)
print(game_no)
print(random.sample(words_list,k = game_no))