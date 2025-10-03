person_0 = {"first_name": "Eren", "last_name": "Tighe", "age": 21, "city": "Womelsdorf"}
person_1 = {"first_name": "Peter", "last_name": "Parker", "age": 18, "city": "Brooklyn"}
person_2 = {"first_name": "Bruce", "last_name": "Wayne", "age": 40, "city": "Gotham"}

people = [person_0, person_1, person_2]
for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("\n")