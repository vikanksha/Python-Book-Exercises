# program calculate the approximate number of atoms that the average person contains, and the percentage of the universe that they comprise.
num_atoms_universe = 10e80
weight_avg_person = 70
num_atoms_avg_person = 7e27
print('This program will determine your place in the universe.')
weight_kg = int(input('Enter your weight in kg:'))
num_atoms = weight_kg * num_atoms_avg_person
percent_of_universe = (num_atoms/num_atoms_universe) * 100
print(num_atoms)
print(percent_of_universe)