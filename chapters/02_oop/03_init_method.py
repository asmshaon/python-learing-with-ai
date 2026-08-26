"""
Chapter 03: Python __init__ Method

===============================

Notes
-----

- __init__ is a special method (constructor) called automatically when an object is created.
- It initializes the object's attributes.
- The first parameter is always self (refers to the new instance).
- You can set default values for parameters in __init__.
- __init__ can accept any number of arguments beyond self.
- It does NOT return a value (implicitly returns None).

Run:
    python3 chapters/02_oop/03_init_method.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Create a class with __init__ that sets two attributes
# ---------------------------------------------------------------------------


def problem_1():

    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age

    person = Person("Abu", 35)

    return {
        "name": person.name,
        "age": person.age,
    }


# ---------------------------------------------------------------------------
# Problem 2: Use default parameter values in __init__
# ---------------------------------------------------------------------------


def problem_2():

    class Person:

        def __init__(self, name="John", age=30):
            self.name = name
            self.age = age

    person = Person()

    return {
        "name": person.name,
        "age": person.age,
    }


# ---------------------------------------------------------------------------
# Problem 3: Compute an attribute inside __init__ from arguments
# ---------------------------------------------------------------------------


def problem_3():

    class Sum:

        def __init__(self, num1, num2):
            self.total = num1 + num2

    result = Sum(10, 20)

    return result.total


# ---------------------------------------------------------------------------
# Run problems
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("Problem 1:", problem_1())

    print("Problem 2:", problem_2())

    print("Problem 3:", problem_3())
