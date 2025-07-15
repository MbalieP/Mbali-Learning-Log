# classes.py

# A class in Python is a blueprint for creating objects.
# It allows you to bundle data (attributes) and functionality (methods) together.

class Dog:
    # Class attribute
    species = "Canis lupus familiaris"  # This is shared by all instances

    def __init__(self, name, age):
        """
        The __init__ method is the class constructor. 
        It initializes the object's attributes when a new object is created.
        
        Parameters:
        name (str): The name of the dog.
        age (int): The age of the dog in years.
        """
        self.name = name  # Instance attribute for the dog's name
        self.age = age    # Instance attribute for the dog's age

    def bark(self):
        """A simple method that makes the dog bark."""
        return f"{self.name} says Woof!"

    def get_human_age(self):
        """
        A method that converts the dog's age to human years.
        Generally, the first two years count as 10.5 years each,
        and each year after that counts as 4 years.
        """
        if self.age <= 2:
            return self.age * 10.5
        else:
            return 21 + (self.age - 2) * 4

# Creating an instance of the Dog class

my_dog = Dog("Buddy", 3)

# Accessing attributes
print(f"My dog's name is {my_dog.name}.")  # Output: My dog's name is Buddy.
print(f"My dog is {my_dog.age} years old.")  # Output: My dog is 3 years old.

# Calling methods
print(my_dog.bark())  # Output: Buddy says Woof!
print(f"My dog's age in human years is {my_dog.get_human_age()} years.")  # Output: My dog's age in human years is 25 years.

# Demonstrating class attribute
print(f"All dogs belong to the species: {my_dog.species}")  # Output: All dogs belong to the species: Canis lupus familiaris
