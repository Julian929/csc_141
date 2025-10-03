rivers = {'Nile': 'Egypt',
          'Amazon': 'Brazil',
          'Yangtse': 'China'}

for river, country in rivers.items():\
print(f"The {river.title()} runs through {country}.")
    
print("\n")

for river in rivers.keys():
    print(river)

print("\n")

for country in rivers.values():
    print(country)