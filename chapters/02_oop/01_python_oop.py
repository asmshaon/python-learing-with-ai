"""
Chapter 01: Python OOP

======================

Notes
-----

- OOP is a programming paradigm based on the concept of "objects".
- Objects contain data (attributes) and code (methods).
- A class is a blueprint for creating objects.
- Key concepts: Class, Object, Method, Attribute.
- OOP helps organize code, reuse logic, and model real-world entities.
- Python supports OOP fully with classes, inheritance, polymorphism, etc.

Run:
    python3 chapters/02_oop/01_python_oop.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Create a simple class with a method and instantiate an object
# ---------------------------------------------------------------------------


def problem_1():
    class Fruit:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    fruit = Fruit("Apple")

    return fruit.get_name()


# ---------------------------------------------------------------------------
# Problem 2: Use class attributes to count objects created
# ---------------------------------------------------------------------------


def problem_2():
    class User:
        count = 0

        def __init__(self):
            User.count += 1

    user1 = User()
    user2 = User()
    user3 = User()
    user4 = User()

    return User.count


# ---------------------------------------------------------------------------
# Problem 3: Demonstrate that methods can return different values per object
# ---------------------------------------------------------------------------


def problem_3():
    class Fruit:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    fruit = Fruit("Apple")
    fruit2 = Fruit("Mango")

    return fruit.get_name(), fruit2.get_name()


# ---------------------------------------------------------------------------
# Run problems
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
