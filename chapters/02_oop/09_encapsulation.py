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
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Use a setter with validation to prevent invalid values
#   Input:  Temperature().set_temp(-10) -> get_temp()
#           Temperature().set_temp(200) -> "Invalid temperature"
#   Output: -10, "Invalid temperature"
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Use property() to create getter/setter without explicit methods
#   Input:  Product("Widget", 25).price = -5 -> "Price cannot be negative"
#           Product("Widget", 25).price = 30 -> Product("Widget", 30).price
#   Output: "Price cannot be negative", 30
# ---------------------------------------------------------------------------
def problem_3():
    pass


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
