class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Calculator:
    # Method overloading simulated with default arguments
    def add(self, a, b=0):
        return a + b

class Person:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Usage
if __name__ == "__main__":
    dog = Dog()
    dog.speak()

    calc = Calculator()
    print(calc.add(5, 10))
    print(calc.add(5))  # Uses default argument

    p = Person()
    p.name = "Mbali"
    print(p.name)

