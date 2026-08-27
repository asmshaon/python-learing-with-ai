"""
Chapter 07: Python Inheritance
===============================

Notes
-----
- Inheritance lets a child class reuse code from a parent class.
- Define a child class with class Child(Parent):.
- The child inherits all attributes and methods from the parent.
- Use super().__init__(...) to call the parent constructor.
- A child can override parent methods by redefining them.
- issubclass(Child, Parent) returns True.

Run:  python3 chapters/02_oop/07_inheritance.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Create a child class that inherits a method from parent
#   Input:  Dog("Rex").speak()
#   Output: "Rex says Woof!"
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Override a parent method in the child class
#   Input:  Cat("Luna").speak()
#   Output: "Luna says Meow!"
#           Cat("Luna").leg_count() -> 4
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Use super() to extend parent behavior instead of replacing it
#   Input:  ElectricCar("Tesla", 75).info()
#   Output: "Tesla, battery: 75kWh, wheels: 4"
# ---------------------------------------------------------------------------
def problem_3():
    pass


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
