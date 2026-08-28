"""
Chapter 09: Python Encapsulation
=================================

Notes
-----
- Encapsulation restricts direct access to some attributes/methods.
- Naming conventions control access:
    public:    name         — accessible from anywhere
    protected: _name        — by convention, internal use only
    private:   __name       — name-mangled by Python, harder to access externally
- Getter methods provide read access; setter methods provide controlled write access.
- Encapsulation protects object integrity and hides implementation details.

Run:  python3 chapters/02_oop/09_encapsulation.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Use a private attribute with a getter method
#   Input:  BankAccount(1000).get_balance()
#   Output: 1000
# ---------------------------------------------------------------------------
import select


def problem_1():
    class BankAccount:
        def __init__(self, balance):
            self.__balance = balance

        def get_balance(self):
            return self.__balance

    ba = BankAccount(1000)

    return ba.get_balance()


# ---------------------------------------------------------------------------
# Problem 2: Use a setter with validation to prevent invalid values
#   Input:  Temperature().set_temp(-10) -> get_temp()
#           Temperature().set_temp(200) -> "Invalid temperature"
#   Output: -10, "Invalid temperature"
# ---------------------------------------------------------------------------
def problem_2():
    class Temperature:

        def set_temp(self, temp):
            if temp >= 200:
                return "Invalid temperature"

            self.__temp = temp

            return self

        def get_temp(self):
            return self.__temp

    t = Temperature().set_temp(-10)

    t2 = Temperature().set_temp(200)

    return t.get_temp(), t2


# ---------------------------------------------------------------------------
# Problem 3: Use property() to create getter/setter without explicit methods
#   Input:  Product("Widget", 25).price = -5 -> "Price cannot be negative"
#           Product("Widget", 25).price = 30 -> Product("Widget", 30).price
#   Output: "Price cannot be negative", 30
# ---------------------------------------------------------------------------
def problem_3():
    class Product:
        def __init__(self, name, price):
            self.__name = name
            self.__price = price

        def set_price(self, price):
            if price < 0:
                return "Price cannot be negative"

            self.__price = price

            return self

        def get_price(self):
            return self.__price

        price = property(get_price, set_price)

    p1 = Product("Widget", 25)

    result = p1.set_price(-5)

    p2 = Product("Widget", 25)
    p2.price = 30

    return result, p2.price


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
