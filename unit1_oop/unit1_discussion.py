"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Computer:
    device_type = "Computer"

    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

    def display_info(self):
        return f"Brand: {self.brand}, Processor: {self.processor}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class GamingComputer(Computer):
    computer_type = "Gaming Computer"

    def __init__(self, brand, processor, gpu, ram):
        super().__init__(brand, processor)
        self.gpu = gpu
        self.ram = ram

    def display_info(self):
        return f"Brand: {self.brand}, Processor: {self.processor}, GPU: {self.gpu}, RAM: {self.ram}GB"

    def gaming_ready(self):
        return f"{self.brand} gaming computer is ready to play."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    computer1 = GamingComputer("Dell", "Intel i7", "RTX 4060", 16)
    computer2 = GamingComputer("HP", "AMD Ryzen 7", "RTX 4070", 32)

    print("Class variable through class:", GamingComputer.computer_type)
    print("Class variable through object:", computer1.computer_type)

    computer1.owner = "Jake"

    print("Computer 1 namespace:", computer1.__dict__)
    print("Computer 2 namespace:", computer2.__dict__)

    print("Class namespace:", GamingComputer.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = {
        "brand": "Dell",
        "components": ["RTX 4060", "16GB RAM", "1TB SSD"]
    }

    shallow = copy(original)
    deep = deepcopy(original)

    original["components"].append("RGB Keyboard")

    print("Original:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)

    # A shallow copy creates a new outer object, but nested mutable objects
    # are still shared with the original.
    # A deep copy creates independent copies of nested mutable objects.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    parent_computer = Computer("Dell", "Intel i5")
    print("\nParent object:")
    print(parent_computer.display_info())

    gaming_computer = GamingComputer("Alienware", "Intel i9", "RTX 4080", 32)
    print("\nChild object:")
    print(gaming_computer.display_info())
    print(gaming_computer.gaming_ready())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()