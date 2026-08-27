"""
Chapter 04: Python self Parameter

==================================

Notes
-----

- 'self' is the first parameter of every instance method in a class.
- It refers to the current object (the instance calling the method).
- Python passes 'self' automatically — you don't pass it when calling.
- You can name it anything, but 'self' is the universal convention.
- Through 'self', you access and modify attributes of the object.

Run:
    python3 chapters/02_oop/04_self_parameter.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Use self to set and return an attribute
#
# Input:  "Alice"
# Output: "Hello, Alice"
# ---------------------------------------------------------------------------


def problem_1():

    class Greetings:

        def __init__(self, name):
            self.greeting = f"Hello, {name}"

    obj = Greetings("Alice")

    return obj.greeting


# ---------------------------------------------------------------------------
# Problem 2: Use self to track a counter across method calls
#
# Input:  click() called 4 times, then get_count()
# Output: 4
# ---------------------------------------------------------------------------


def problem_2():

    class Counter:

        def __init__(self):
            self.count = 0

        def click(self):
            self.count += 1

        def get_count(self):
            return self.count

    counter = Counter()

    counter.click()
    counter.click()
    counter.click()
    counter.click()

    return counter.get_count()


# ---------------------------------------------------------------------------
# Problem 3: Use self to compare two attributes set in __init__
#
# Input:  Wall(10, 5) -> is_square()
# Output: False
# ---------------------------------------------------------------------------


def problem_3():

    class Wall:

        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def is_square(self):
            return self.num1 == self.num2

    wall = Wall(10, 5)

    return wall.is_square()


# ---------------------------------------------------------------------------
# Run problems
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("Problem 1:", problem_1())

    print("Problem 2:", problem_2())

    print("Problem 3:", problem_3())
