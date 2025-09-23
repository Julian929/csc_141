guests = ["Simon Peter", "John the Baptist", "King David",]

guests[0] = "Moses"

guests.insert(0, "King Solomon")
guests.insert(4, "Isaiah")
guests.append("Zaccheus")

print(guests)

print(f"Just learned the big table won't be ready in time and there's only space for two people.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you anymore.")
popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you anymore.")
popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you anymore.")
popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you anymore.")

print(guests)
print(popped_guest)

print(f"Hi {guests[0]}, you and {guests[1]} are still invited.")
print(f"Hi {guests[1]}, you and {guests[0]} are still invited.")

print(len(guests))