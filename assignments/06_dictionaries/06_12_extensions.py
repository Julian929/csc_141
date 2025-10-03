pet_0 = {'animal': 'dog', 'color': 'brown', 'collar color': 'blue', 'size': 'large', 'owner': 'Bob'}
pet_1 = {'animal': 'cat', 'color': 'grey', 'collar color': 'red', 'size': 'tiny', 'owner': 'Dylan'}

pets = [pet_0, pet_1]

for pet in pets:
    print(f"The pet is a {pet['size']}, {pet['color']} {pet['animal']}. The owner is {pet['owner']} and he gave him a {pet['collar color']} collar.")