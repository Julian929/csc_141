glossary = {'string': 'sequence of chaacters wrapped in quotes',
            'boolean': 'truth values - either True or False',
            'list': 'mutable ordered sequence of elemnts',
            'tuple': 'immutable ordered sequence of values',
            'dictionary': 'collection of a key-value pairs'}

for key, value in glossary.items():
    print(f"{key.title()}: {value}: ")

