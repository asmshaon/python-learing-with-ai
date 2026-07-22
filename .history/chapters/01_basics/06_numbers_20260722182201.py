"""
Chapter 06: Python Numbers
==========================

Notes
-----
- Python has three numeric types:
      int       7, -3, 0          unlimited precision (no overflow!)
      float     7.0, -0.5, 2e3    64-bit double; 2e3 means 2 * 10**3 = 2000.0
      complex   3+2j              j is the imaginary unit; has .real and .imag
- Division ALWAYS returns a float: 8 / 2 is 4.0, not 4. Use // for floor
  (integer) division: 8 // 2 is 4, and 7 // 2 is 3 (rounds DOWN, so
  -7 // 2 is -4, not -3).
- The % (modulo) operator gives the remainder: 7 % 3 is 1. The result takes
  the SIGN of the divisor in Python: -7 % 3 is 2 (unlike many languages).
- ** is exponentiation: 2 ** 10 is 1024. It binds tighter than unary minus,
  so -2 ** 2 is -4, and (-2) ** 2 is 4.
- Floats are approximate: 0.1 + 0.2 == 0.3 is False, because 0.1 has no
  exact binary representation. Compare floats with math.isclose(a, b) or
  round(a, ndigits) == round(b, ndigits), never with ==.
- Mixing types promotes to the "wider" type: int + float -> float,
  float + complex -> complex.
- Useful built-ins (no import needed):
      abs(-5)          -> 5
      round(2.675, 2)  -> 2.67  (banker's rounding: ties go to the EVEN digit,
                                 so round(0.5) is 0 and round(1.5) is 2)
      divmod(7, 3)     -> (2, 1)  quotient and remainder at once
      pow(2, 10)       -> 1024   (pow(2, 10, 5) also does modular arithmetic)
      min(...), max(...), sum([...])
- Conversions: int("42"), float("2.5"), int(2.9) truncates toward zero -> 2.

Run:  python3 chapters/01_basics/06_numbers.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Division operators
# Given two numbers a and b, return a tuple of four results, in this order:
#     a / b     true division  (always float)
#     a // b    floor division
#     a % b     remainder
#     divmod(a, b)   the (quotient, remainder) pair
# (Test with a=17, b=5 -> expected (3.4, 3, 2, (3, 2)))
# ---------------------------------------------------------------------------
import math
from statistics import mean


def problem_1(a=17, b=5):
    return (a / b, a // b, a % b, divmod(a, b))


# ---------------------------------------------------------------------------
# Problem 2: Float precision
# Return a tuple of three booleans, in this order:
#     0.1 + 0.2 == 0.3                          -> False (float surprise!)
#     round(0.1 + 0.2, 10) == round(0.3, 10)    -> True  (safe comparison)
#     math.isclose(0.1 + 0.2, 0.3)              -> True  (the proper tool)
# You will need:  import math  (put the import inside the function).
# (expected (False, True, True))
# ---------------------------------------------------------------------------
def problem_2():
    return (
        0.1 + 0.2 == 0.3,
        round(0.1 + 0.2, 10) == round(0.3, 10),
        math.isclose(0.1 + 0.2, 0.3)
    )


# ---------------------------------------------------------------------------
# Problem 3: Number stats without loops
# Given a list of numbers, return a dict with these keys:
#     "min"   smallest value          -> min()
#     "max"   largest value           -> max()
#     "sum"   total                   -> sum()
#     "mean"  average, ROUNDED to 2 decimal places -> round(sum/len, 2)
#     "abs"   a list of each value's absolute value -> abs() on each
# (Test with [3, -7, 1.5, 10, -2]
#  -> expected {'min': -7, 'max': 10, 'sum': 5.5, 'mean': 1.1,
#               'abs': [3, 7, 1.5, 10, 2]})
# ---------------------------------------------------------------------------
def problem_3(numbers=(3, -7, 1.5, 10, -2)):
    myDic = {}

    myDic['min'] = min(numbers)
    myDic['max'] = max(numbers)
    myDic['sum'] = sum(numbers)
    myDic['mean'] = mean(numbers)
    myDic['abs'] = abs(numbers)

    return myDic


if __name__ == "__main__":
    print("Problem 1 (division):", problem_1())
    print("Problem 2 (float precision):", problem_2())
    print("Problem 3 (stats):", problem_3())
