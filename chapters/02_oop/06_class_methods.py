"""
Chapter 06: Python Class Methods
=================================

Notes
-----
- A class method receives the class itself as the first argument (not the instance).
- Decorate it with @classmethod.
- First param is conventionally named 'cls' (refers to the class, not the object).
- Class methods can create alternative constructors (factory methods).
- They can access/modify class-level state, not instance-level state.

Run:  python3 chapters/02_oop/06_class_methods.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Create a class method that returns a string representation
#   Input:  Email.from_string("alice@example.com")
#   Output: "Email: alice@example.com"
# ---------------------------------------------------------------------------
def problem_1():
    class Email:

        def __init__(self, email):
            self.email = email

        @classmethod
        def from_string(cls, email):
            return cls(email)

        def __str__(self):
            return f"Email: {self.email}"

    return Email.from_string("alice@example.com")


# ---------------------------------------------------------------------------
# Problem 2: Use a class method as a factory to create objects from a dict
#   Input:  Player.from_dict({"name": "Sam", "score": 100}) -> player.name
#   Output: "Sam"
# ---------------------------------------------------------------------------
def problem_2():
    class Player:

        def __init__(self, name):
            self.name = name

        @classmethod
        def from_dict(cls, player):
            return cls(player.get("name"))

        def __str__(self):
            return f"{self.name}"

    return Player.from_dict({"name": "Sam", "score": 100})


# ---------------------------------------------------------------------------
# Problem 3: Use a class method to modify class-level state
#   Input:  BankAccount.set_interest(0.05), then create account, return account.interest
#   Output: 0.05
# ---------------------------------------------------------------------------
def problem_3():
    class BankAccount:
        interest = 0

        def __init__(self):
            pass

        @classmethod
        def set_interest(cls, interest):
            cls.interest = interest

    BankAccount.set_interest(0.05)

    account = BankAccount

    return account.interest


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
