favorite_places = {'Eren': ['Spain', 'Portugal'],
                   'Peter': ['Spain'],
                   'Lisa':['Tokyo', 'Bali', 'Toronto']}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"\t{place}")
    print("\n")