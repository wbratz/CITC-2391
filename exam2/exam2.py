cities = {'GA' : 'Atlanta', 'NY' : 'Albany', 'CA' : 'San Diego'}
if 'CA' in cities:
    del cities['CA']
cities['CA'] = 'Sacramento'
print(cities)