print("Enter rwo numbers to add them.")
print("Enter 'q' to stop execution.")

while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter second number: ")
    if num2 == 'q':
        break

    try:
        result = int(num1) + int(num2)
        print(f"The result is: {result}")
    except ValueError:
        print("Wromg value provided. Enter two numbers.")
