filename = 'guest_book.txt'

print("Please enter the guest names.")
print("Type 'q' when you are finished.")

while True:
    name =input("Enter your name: ")

    if name == 'q':
        break
    else:
        print(f"Welcome {name}.")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
