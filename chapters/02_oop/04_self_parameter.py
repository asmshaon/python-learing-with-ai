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

Run:  python3 chapters/02_oop/04_self_parameter.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Use self to set and return an attribute
#   Input:  "Alice"
#   Output: "Hello, Alice"
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Use self to track a counter across method calls
#   Input:  click() called 4 times, then get_count()
#   Output: 4
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Use self to compare two attributes set in __init__
#   Input:  Wall(10, 5) -> is_square()
#   Output: False
# ---------------------------------------------------------------------------
def problem_3():
    pass


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
