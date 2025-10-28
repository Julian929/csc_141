class Restaurant:
    """A simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type arguments."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes a restairant."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restairant(self):
        """Describes that restaurant is open."""
        print(f"The resturant {self.restaurant_name} is open.")

    restaurant = Restaurant('Basserie', 'French')
    print(f"Restaurant name: {restaurant.restaurant_name}.")
    print(f"Restaurant cuisine: {restaurant.cuisine_type}.")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()