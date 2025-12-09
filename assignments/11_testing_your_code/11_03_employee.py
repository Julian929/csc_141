class Employee:
    """Store employee information (name, salary)."""

    def __init__(self, first_name, last_name, salary):
        """Store a first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """Add at least $5,000 to anual salary."""
        self.salary += salary_raise

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Create an employee entry with a first name, last name and salary for use in all test methods."""
        first_name = 'John'
        last_name = 'Doe'
        self.salary = 50000
        self.employee = Employee(first_name, last_name, self.salary)

    def test_give_default_raise(self):
        """Test that default raise works properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.salary + 5000)

    def test_give_default_raise(self):
        """Test that default raise works properly."""
        custom_raise = 10000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.salary, self.salary + custom_raise)

if __name__ == '__main__':
    unittest.main()