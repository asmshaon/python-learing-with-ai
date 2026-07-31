"""
Chapter 15: Python If...Else
============================

Notes
-----
- Conditions decide which block runs. INDENTATION marks the block — there are
  no braces:
      if age >= 18:
          print("adult")
      elif age >= 13:
          print("teen")
      else:
          print("child")
- elif is checked only when every condition above it was False, and at most one
  branch of the whole chain ever runs. Order matters: put the most specific
  test first.
- Comparison operators:  ==  !=  <  <=  >  >=
  Chaining works and reads naturally:  0 <= score <= 100
- Combining conditions:  and  or  not
  "and" / "or" SHORT-CIRCUIT — they stop as soon as the answer is known, so
      if items and items[0] == "x":
  is safe on an empty list.
- Truthiness: anything can be used as a condition. Falsy values are
      False, None, 0, 0.0, "", [], (), {}, set()
  everything else is truthy. So "if items:" means "if items is not empty".
- The ternary (conditional expression) picks a VALUE in one line:
      label = "even" if n % 2 == 0 else "odd"
- pass is a do-nothing placeholder for a block you have not written yet:
      if broken:
          pass
- Nested ifs are fine, but flat is usually clearer — an early return often
  beats another level of indentation.
- Watch out: = is assignment, == is comparison. Use "is" / "is not" only for
  None and other singletons, not for numbers or strings.

Run:  python3 chapters/01_basics/15_if_else.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Grade classifier
# Given a score, return its letter grade using an if/elif/else chain:
#     90 and above -> "A"      80-89 -> "B"      70-79 -> "C"
#     60-69        -> "D"      below 60 -> "F"
# If the score is outside 0-100, return "invalid" instead.
# (Test with 85 -> "B"; also check 100, 59, -5 and 101)
# ---------------------------------------------------------------------------
import re
from typing import final


def problem_1(score=-5):
    if score < 0 or score > 100:
        return "invalid"
    elif score >= 90:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------------------------
# Problem 2: Truthiness and the ternary
# Given any value, return a dict describing it:
#     "truthy"  -> True/False, whether the value is truthy
#     "kind"    -> "empty" if it is falsy, otherwise "filled"  (use a ternary)
#     "sign"    -> for numbers: "positive" / "negative" / "zero";
#                  for anything else: "not a number"
# Booleans count as numbers in Python — treat True as 1 and False as 0 here.
# (Test with 0 -> {'truthy': False, 'kind': 'empty', 'sign': 'zero'};
#  also check "hi", [], -3)
# ---------------------------------------------------------------------------
def problem_2(value=0):
    number_flag = ""

    if isinstance(value, (int, float)):
        if value < 0:
            number_flag = "negative"
        elif value == 0:
            number_flag = "zero"
        else:
            number_flag = "positive"
    else:
        number_flag = "not a number"

    return {
        "truthy": bool(value),
        "kind": "filled" if value else "empty",
        "sign": number_flag,
    }


# ---------------------------------------------------------------------------
# Problem 3: Combining conditions
# A ticket price depends on age and the day:
#     under 5           -> free (0)
#     5 to 17, or 65+   -> 5
#     everyone else     -> 10
# Then: on "tuesday" every non-free ticket gets 2 taken off, and a member gets
# 20% off the price AFTER that discount (round to 2 decimals).
# Return a dict with "base", "after_day", "final".
# Use and/or to keep the branches short.
# (Test with age=70, day="tuesday", member=True
#  -> expected {'base': 5, 'after_day': 3, 'final': 2.4})
# ---------------------------------------------------------------------------
def problem_3(age=7, day="tuesday", member=True):
    base = 0

    if age < 5:
        base = 0
    elif (5 <= age <= 17) or age >= 65:
        base = 5
    else:
        base = 10

    after_day = base - 2 if day == "tuesday" else base

    final = round(after_day * 0.8, 2) if member else after_day

    return {"base": base, "after_day": after_day, "final": final}


if __name__ == "__main__":
    print("Problem 1 (grades):", problem_1())
    print("Problem 2 (truthiness):", problem_2())
    print("Problem 3 (ticket price):", problem_3())
