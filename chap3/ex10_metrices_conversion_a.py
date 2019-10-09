#for convesion from pound to gms we have to firstly convert in kg then kg convert in gms. 
pounds = int(input("Enter value in pound:"))
pound_to_kg = pounds / 2.2
kg_to_gm = pound_to_kg * 1000
print(kg_to_gm)