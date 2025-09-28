pizzas =["Cheese", "Pepperoni", "Margarita"]
friend_pizzas = pizzas[:]

pizzas.append("hawaiian")
friend_pizzas.append("meat lovers")

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print(f"My friend's favorite pizza is:")
for pizza in friend_pizzas:
    print(pizza)