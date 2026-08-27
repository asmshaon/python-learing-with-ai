"""
Chapter 08: Python Polymorphism
================================

Notes
-----
- Polymorphism means "many forms" — same method name, different behavior.
- Achieved via method overriding: child redefines a parent method.
- Works because Python uses dynamic dispatch (decides at runtime which method to call).
- Built-in examples: len() works on lists, strings, dicts — same function, different types.
- Enables writing generic code that works with any object that has the right method.

Run:  python3 chapters/02_oop/08_polymorphism.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Two different classes with the same method name, called via a list
#   Input:  [Dog(), Cat()].speak() for each
#   Output: ["Woof!", "Meow!"]
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Write a function that works with any object having a .value attribute
#   Input:  total([Price(10), Price(20), Price(5)])
#   Output: 35
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Use isinstance() to handle different types differently
#   Input:  describe(Car("Toyota")) -> "A car"
#           describe(Bike("Trek"))  -> "A bike"
# ---------------------------------------------------------------------------
def problem_3():
    pass


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
