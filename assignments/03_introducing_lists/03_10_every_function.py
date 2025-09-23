things = ["shoes", "bed", "table", "computer", "poster","tv"]
print(things[0])
print(things[1])
print(things[2])
print(things[3])
print(things[4])
print(things[5])

print(f"I have 10 pairs of {things[0]}.")
print(f"My {things[1]} is very comfortbale.")
print(f"I am currently sitting at a {things[2]}.")
print(f"My {things[3]} is slow.")
print(f"There is 15 {things[4]}s in my dorm rooom.")
print(f"I watch {things[5]} when I am feeling bored or lazy.")

things[0] = "chair"
print(f"I am sitting in a {things[0]}.")

things.insert(4, "headphones")
things.append("blanket")
print(f"I always wear {things[4]} because I love listening to music.")
print(f"It's cold in my room so I use a {things[7]}.")

popped_things = things.pop()
pooped_things = things.pop()
popped_things = things.pop()
print(things)

print(things)
print(sorted(things))
print(things)
things.reverse()
print(things)
things.reverse()
print(things)
things.sort()
print(things)
things.sort(reverse=True)
print(things)

print(len(things))