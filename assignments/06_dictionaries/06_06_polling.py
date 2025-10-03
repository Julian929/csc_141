favorite_languages = {'Julian': 'Python',
                      'Braden': 'C',
                      'Jude': 'Ruby',
                      'Drew': 'Python'}

people = ['Julian', 'Braden', 'Vince']
for person in people:
    if person in favorite_languages.keys():
        print(f"Hey {person}, thank you for taking the poll.")
    else:
        print(f"Hey {person}, please take the poll.")