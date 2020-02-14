import copy
print("Lista de pýthon ...")

countries = ['Mexico', 'Vemnezuela', 'Colombia', 'Argentina']
ages = [12, 18, 24, 34, 50]
print(countries)
countries[0] = 'Ecuador'
print(countries)

global_countries = countries
print(global_countries)
countries[0] = 'Guatemala'
print(global_countries)
# copy function
global_countries = None
global_countries = copy.copy(countries)
print(global_countries)
countries[0] = 'Honduras'
print(global_countries)

for country in countries:
	print(country)