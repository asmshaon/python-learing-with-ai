"""
Chapter 10: Python Inner Classes
=================================

Notes
-----
- An inner class is a class defined inside another class.
- It is scoped to the outer class and accessed via it.
- Useful when the inner class only makes sense in context of the outer class.
- Access outer class attributes via the outer instance passed to the inner class.
- Common use cases: iterators, nodes in linked lists, components of a larger object.

Run:  python3 chapters/02_oop/10_inner_classes.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Create an inner class and access it from the outer class
#   Input:  LinkedList().add(10).add(20) -> LinkedList().head.value
#   Output: 10
# ---------------------------------------------------------------------------


def problem_1():
    class LinkedList:

        def __init__(self):
            self.head = None

        class Head:

            def __init__(self, value):
                self.value = value

        def add(self, value):
            self.head = self.Head(value)

            return self

    linked_list = LinkedList().add(10).add(20)

    return linked_list.head.value


# ---------------------------------------------------------------------------
# Problem 2: Use inner class to build a composite object
#   Input:  ShoppingCart().add_item("apple", 2).total_price()
#   Output: 6.0
# ---------------------------------------------------------------------------
def problem_2():

    class ShoppingCart:

        class Item:

            def __init__(self, name, price):
                self.name = name
                self.price = price

        def __init__(self):
            self.item = None

        def add_item(self, name, price):
            self.item = self.Item(name, price)
            return self

        def total_price(self):
            return 3 * self.item.price

    sc = ShoppingCart().add_item("apple", 2).total_price()

    return sc


# ---------------------------------------------------------------------------
# Problem 3: Inner class holds a reference back to outer class
#   Input:  University().add_student("Alice").get_info()
#   Output: "Alice at University"
# ---------------------------------------------------------------------------
def problem_3():
    class University:

        class Student:

            def __init__(self, name):
                self.name = name

        def add_student(self, name):
            self.student = self.Student(name)

            return self

        def get_info(self):
            return f"{self.student.name} at University"

    u = University().add_student("Alice").get_info()

    return u


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
