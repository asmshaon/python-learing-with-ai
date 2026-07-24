"""
Chapter 07: Python Casting
==========================

Notes
-----
- Casting means converting a value to another type by CALLING the type as a
  constructor: int(x), float(x), str(x), bool(x), list(x), tuple(x), set(x).
- int() rules:
      int("42")     -> 42      digits-only strings work (spaces are stripped)
      int("4.2")    -> ValueError!  int() will NOT parse a float-looking string
      int(4.9)      -> 4       floats TRUNCATE toward zero (not floor/round)
      int(-4.9)     -> -4      (truncation, so it goes toward 0, not to -5)
      int("ff", 16) -> 255     optional base argument for other number bases
- float() rules:
      float("2.5")  -> 2.5
      float("2")    -> 2.0
      float(7)      -> 7.0
- str() works on ANYTHING and never fails: str(3.14) -> "3.14",
  str([1, 2]) -> "[1, 2]", str(None) -> "None".
- bool() follows the FALSY list — these become False:
      0, 0.0, "", [], (), {}, set(), None, False
  everything else becomes True, including "0" and "False" (non-empty strings!)
  and [0] (non-empty list).
- Casting between collections:
      list("abc")       -> ['a', 'b', 'c']    a string is a sequence of chars
      tuple([1, 2])     -> (1, 2)
      set([1, 2, 2, 1]) -> {1, 2}             deduplicates (order not kept)
      list(range(3))    -> [0, 1, 2]
- A failed numeric cast raises ValueError — catch it with try/except when
  input is untrusted (full try/except is covered later; a taste appears here).

Run:  python3 chapters/01_basics/07_casting.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Round-trip conversions
# Return a tuple of five results, in this order:
#     int("42")        the string "42" as an int
#     float("2.5")     the string "2.5" as a float
#     str(3.14)        the float 3.14 as a string
#     int(9.99)        truncation, NOT rounding
#     int(-9.99)       truncation goes toward zero
# (expected (42, 2.5, '3.14', 9, -9))
# ---------------------------------------------------------------------------
def problem_1():
    return (
        int("42"),
        float("2.5"),
        str(3.14),
        int(9.99),
        int(-9.99)
    )


# ---------------------------------------------------------------------------
# Problem 2: Truthiness table
# Given a list of values, return a list of their bool() results in order.
# Watch out: "0" and "False" are non-empty strings, so they are truthy!
# (Test with [0, 1, "", "0", "False", [], [0], None, 0.0]
#  -> expected [False, True, False, True, True, False, True, False, False])
# ---------------------------------------------------------------------------
def problem_2(values=(0, 1, "", "0", "False", [], [0], None, 0.0)):
    return [bool(value) for value in values]


# ---------------------------------------------------------------------------
# Problem 3: Safe int parsing
# Given a list of strings, try to cast each to int. Return a dict mapping each
# string to its int value, or to None if the cast raises ValueError.
# Skeleton for the body of the loop:
#     try:
#         result[s] = int(s)
#     except ValueError:
#         result[s] = None
# (Test with ["10", "abc", "-3", "4.2", "007"]
#  -> expected {'10': 10, 'abc': None, '-3': -3, '4.2': None, '007': 7})
# ---------------------------------------------------------------------------
def problem_3(strings=("10", "abc", "-3", "4.2", "007")):
    result = {}

    for s in strings:
        try:
            result[s] = int(s)
        except ValueError:
            result[s] = None

    return result

if __name__ == "__main__":
    print("Problem 1 (round-trip):", problem_1())
    print("Problem 2 (truthiness):", problem_2())
    print("Problem 3 (safe parsing):", problem_3())
