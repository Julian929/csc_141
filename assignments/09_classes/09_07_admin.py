class User:
    """A simple user class."""

    def __init__(self, first_name, last_name, location, age):
        """Initialize sure class and strributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        """Describes a user."""
        print(f"The user's name is {self.first._name} {self.last_name}.")
        print(f"The user is {self.age} years old and lives in {self.location}.")

    def greet_user(self):
        """Greets a user."""
        print(f"Hello {self.first_name} {self.last_name}!")

class Admin(User):
    """A simple admin class."""

    def __init__(self, first_name, last_name, location, age, privelages):
        """Initializes admin class and attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.privelages = privileges
    
    def show_privileges(self):
        """Display privileges."""
        print("Privileges:")
        for privelege in self.privileges:
            print(f"- {privilege}")