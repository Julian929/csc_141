prompt = "Which pizza topping would you like?"
prompt += "(Type 'quit' to stop adding toppings)"

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")