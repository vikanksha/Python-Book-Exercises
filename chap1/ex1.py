#the Drake equation, developed by frank Drake in the 1960s, attempta to estimate how many extraterrestrial civilization, N, may exist  in our galaxy.
# N = R*p*n*f*i*c*L
# R's value is 7,per year.
p = int(input("what percentage of star do you think have planets? :"))
n = int(input("how many planets per star do you think can support life? :"))
f = int(input("what percentage do you think actually develop life? :"))
i = int(input("what percentage of those do you think have intelligence life? :"))
c = int(input("what perentage of those do you think can communicate with us? :"))
L = int(input("Number of years you think civilization last? :"))
num_detectable_civilizations = 7*(p/100)*n*(f/100)*(i/100)*(c/100)*L
print(num_detectable_civilizations)