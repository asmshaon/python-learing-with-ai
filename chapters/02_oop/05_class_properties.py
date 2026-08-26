"""
Chapter 05: Python Class Properties
====================================

Notes
-----
- Class attributes are shared by ALL instances of the class.
- Instance attributes belong to a single object (set via self.name = ...).
- Class attributes are defined directly inside the class, outside any method.
- Access with ClassName.attr or self.attr (instance falls back to class).
- Useful for constants, counters, or default values shared across objects.

Run:  python3 chapters/02_oop/05_class_properties.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Define a class attribute as a constant and access it
#   Input:  Dog.MAX_LEGS
#   Output: 4
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Use a class attribute to count total instances created
#   Input:  create 5 Player objects, return Player.total
#   Output: 5
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Override a class attribute in one instance, keep it for others
#   Input:  s1 = Server(); s2 = Server(); s1.port = 8080; return (s1.port, s2.port)
#   Output: (8080, 3000)
# ---------------------------------------------------------------------------
def problem_3():
    pass


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
