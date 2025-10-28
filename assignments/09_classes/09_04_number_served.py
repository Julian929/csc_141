class Restaurant:
    """A simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type arguments."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes a restairant."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restairant(self):
        """Describes that restaurant is open."""
        print(f"The resturant {self.restaurant_name} is open.")

    def set_number_served(self, guests):
        """Set the number of served customers to a given value."""
        self.number_served = guests

    def increment_number_served(self, increment):
        """Set the number of served customers to a given value."""
        self.number_served += increment

restaurant = Restaurant('Brasserie', 'French')
print(f"Number served {restaurant.number_served}")

restaurant.number_served = 200
print(f"Number served: {restaurant.number_served}")
