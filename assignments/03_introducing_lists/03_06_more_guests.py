guests = ["Simon Peter", "John the Baptist", "King David",]

print(f"Hi {guests[0]}, I love the letters you wrote! Would you like to have dinner at my house?")
print(f"Wow, {guests[1]}! Let's have a meal together. I'd love to try locusts and honey.")
print(f"{guests[2]}! What's it like to be called the man after God's heart? I'd love to chat over dinner.")

guests[0] = "Moses"
print(f"Hi {guests[0]}, looks like Peter can't make it. Would you like to come have dinner?")
print(f"Hi {guests[1]}, are we still on for dinner?")
print(f"Hi {guests[2]}, just making sure you can still come to dinner.")

print(f"Hey everyone, I found a bigger table so I'm going to invite more people.")

guests.insert(0, "King Solomon")
guests.insert(4, "Isaiah")
guests.append("Zaccheus")

print(f"Hi {guests[0]}, Would you like to come to dinner? Your dad will be there!")
print(f"{guests[1]}! Lead us to the dinner table!.")
print(f"Hey {guests[2]}, no locusts and honey this time unfortunately.")
print(f"Hi {guests[3]}, we'll head out soon.")
print(f"Hi {guests[4]}, would you like to have dinner?")
print(f"Hi {guests[5]}, would you like to have dinner?")