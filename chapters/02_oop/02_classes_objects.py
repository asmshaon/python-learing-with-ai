"""
Chapter 02: Python Classes/Objects
==================================

Notes
-----
- A class is defined using the 'class' keyword.
- An object is an instance of a class.
- Attributes are variables belonging to an object (accessed with dot notation).
- Methods are functions defined inside a class (first param is usually 'self').
- 'self' refers to the current instance of the class.
- You can create multiple objects from the same class, each with its own data.

Run:  python3 chapters/02_oop/02_classes_objects.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Create a Car class and access its attributes
# ---------------------------------------------------------------------------
def problem_1():
    class Car:
        def __init__(self, model):
            self.model = model

    car1 = Car("Toyota")

    return car1.model


# ---------------------------------------------------------------------------
# Problem 2: Add a method that uses object attributes
# ---------------------------------------------------------------------------
def problem_2():
    class Car:
        def __init__(self, model):
            self.model = model

        def get_model(self):
            return self.model

    car1 = Car("Roles")

    return car1.get_model()


# ---------------------------------------------------------------------------
# Problem 3: Modify attributes after object creation
# ---------------------------------------------------------------------------
def problem_3():
    class Car:
        def __init__(self, model):
            self.model = model

        def set_model(self, model):
            self.model = model

        def get_model(self):
            return self.model

    car1 = Car("Toyota")
    car1.set_model("HOrnet")

    return car1.get_model()


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
