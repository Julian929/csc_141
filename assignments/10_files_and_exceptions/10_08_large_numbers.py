filename1 = 'cats.txt'
filename2 = 'dogs.txt'

print("Cats: ")
try:
    with open(filename1, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename1} does not exist.")
else:
    print(contents)

print("Dogs: ")
try:
    with open(filename2, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename2} does not exist.")
else:
    print(contents)
