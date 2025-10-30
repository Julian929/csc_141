sandwich_orders = ['tuna', 'chicken', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("Sorry, we ran out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("--- Finished sandwiches ---")
for sandwich in finished_sandwiches:
    print(f"We made a {sandwich} sandwich.")
