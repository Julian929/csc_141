favorite_numbers = {'Julian': [14, 7], 
                   'Jesus': [7, 3], 
                   'Jalen': [3, 6],
                   'Markel': [21, 12],
                   'Eren': [20, 22]}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
    print("\n")