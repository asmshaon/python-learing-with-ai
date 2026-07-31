"""
Chapter 09: Python Booleans
===========================

Notes
-----
- There are exactly two boolean values: True and False (capitalized). They are
  a subtype of int, so True == 1 and False == 0 (True + True -> 2).
- bool(x) evaluates the "truthiness" of any value:
      Falsy: False, None, 0, 0.0, "" (empty string), [] {} () set()  (empties)
      Truthy: everything else (non-zero numbers, non-empty containers, objects)
- Comparison operators return booleans:
      ==  !=  <  >  <=  >=      and  x in container  /  x is y (identity)
- Boolean (logical) operators combine conditions:
      and  -> True only if BOTH sides are truthy
      or   -> True if EITHER side is truthy
      not  -> flips the value
- and/or SHORT-CIRCUIT and return an operand, not always a strict bool:
      "a" and "b" -> "b"      (and returns the last value if all truthy)
      "" or "def" -> "def"    (or returns the first truthy value)
  This makes `name or "guest"` a handy default-value idiom.
- Many built-ins answer boolean questions:
      any(iterable) -> True if at least one element is truthy
      all(iterable) -> True if every element is truthy (True for empty!)
      isinstance(x, int), str.isdigit(), str.startswith(...), etc.

Run:  python3 chapters/01_basics/09_booleans.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Truthiness table
# Given a list of assorted values, return a list of (value, bool(value)) pairs
# so you can see which values are truthy and which are falsy.
# (Test with the default list
#  -> expected [(0, False), (1, True), ('', False), ('hi', True),
#               ([], False), ([0], True), (None, False), (3.14, True)])
# ---------------------------------------------------------------------------
import re


def problem_1(values=(0, 1, "", "hi", [], [0], None, 3.14)):
    return [(value, bool(value)) for value in values]


# ---------------------------------------------------------------------------
# Problem 2: Leap year check
# A year is a leap year if it is divisible by 4, EXCEPT century years, which
# must also be divisible by 400. So 2000 and 2024 are leap years; 1900 is not.
# Return True or False using boolean operators.
# (Test defaults: 2024 -> True; try 1900 -> False, 2000 -> True, 2023 -> False)
# ---------------------------------------------------------------------------
def problem_2(year=2024):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# ---------------------------------------------------------------------------
# Problem 3: any / all summary of a data set
# Given a list of numbers, return a dict describing it:
#     "all_positive"  True if every number is > 0
#     "any_negative"  True if at least one number is < 0
#     "all_even"      True if every number is even
#     "has_zero"      True if 0 appears in the list
# (Test with [2, 4, 6, -1]
#  -> expected {'all_positive': False, 'any_negative': True,
#               'all_even': False, 'has_zero': False})
# ---------------------------------------------------------------------------
def problem_3(numbers=(2, 4, 6, -1)):
    return {
        "all_positive": all(n > 0 for n in numbers),
        "any_negative": any(n < 0 for n in numbers),
        "all_even": all(n % 2 == 0 for n in numbers),
        "has_zero": any(n == 0 for n in numbers),
    }


if __name__ == "__main__":
    print("Problem 1 (truthiness):", problem_1())
    print("Problem 2 (leap year):", problem_2())
    print("Problem 3 (any/all):", problem_3())
