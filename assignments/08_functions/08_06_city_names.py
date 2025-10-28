def city_country(city, country):
    """Return formated city, country name."""
    return f"{city.title()}, {country.title()}"

print(city_country("New York", "united states"))
print(city_country("london", "united kingdom"))
print(city_country('berlin', 'gErmany'))