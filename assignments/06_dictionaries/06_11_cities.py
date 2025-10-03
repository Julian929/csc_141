cities = {'Philadelphia': {'country': 'United States', 'population': '1.6m', 'languages': 'There are 41 languages spoken in Philly'},
          'Chicago': {'country': 'United States', 'population': '2.7m', 'languages': 'There are over 40 languages spoken in Chicago'},
          'Baltimore': {'country': 'United States', 'population': '568,000', 'languages': 'There are 17-18 languages spoken in Baltimore'}}

for city, details in cities.items():
    print(f"{city} is located in {details['country']}, and has a population of {details['population']}.")
    print(f"Fact about {city}: {details['languages']}\n")