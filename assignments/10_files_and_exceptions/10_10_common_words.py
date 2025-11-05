filename = 'wealth_of_nations.txt'

with open(filename) as f:
    contents = f.read()

print(contents.lower().count('the'))