#In Python you can create and work with variables.
#You can work with lists and dictionaries.
#You can use conditional atementes using if, elif, and else.
#You can work with user input.
#You can create functions and classes.
#You can read and work with files.

filename = 'learning_python.txt'

with open(filename) as file_object:
    content = file_object.read()
    print(content)

print('---')

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip)

print('---')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())