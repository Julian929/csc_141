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

class IceCreamStand(Restaurant):
    """A simple ice cream stand (onheriting from the restaurant class)."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavor(self):
        """Dsiplay ice cream flavor."""
        print(f"The flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream = IceCreamStand('ice cream parlor', 'ice cream', ['vanilla', 'chocolate'])
ice_cream.display_flavor()
