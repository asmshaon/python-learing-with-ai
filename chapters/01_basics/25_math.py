"""
Chapter 25: Python Math
=======================

Notes
-----
- Some maths is BUILT IN, no import needed:
      min(a, b, ...)   smallest       max(a, b, ...)   largest
      abs(x)           distance from zero
      sum(iterable)    total
      round(x, n)      round to n decimal places (n is optional)
      pow(x, y)        same as x ** y
  min/max/sum also take a list directly: min([4, -17, 23]).
- Everything else lives in the math module:  import math
- ROUNDING has three different tools, and they disagree on purpose:
      math.ceil(7.2)   -> 8    always UP to the next whole number
      math.floor(7.8)  -> 7    always DOWN
      math.trunc(-3.7) -> -3   chops the decimals off, toward zero
      round(7.5)       -> 8    to the nearest, ties go to the EVEN number
  Watch the negatives: floor(-3.7) is -4 but trunc(-3.7) is -3.
- ROOTS and POWERS:
      math.sqrt(144)   -> 12.0   (a float, always)
      math.isqrt(50)   -> 7      whole-number square root, rounded down
      math.pow(2, 10)  -> 1024.0 (float)   vs   2 ** 10 -> 1024 (int)
- WHOLE-NUMBER helpers:
      math.factorial(6)   6*5*4*3*2*1
      math.gcd(48, 60)    greatest common divisor
      math.lcm(4, 6)      lowest common multiple
      math.comb(5, 2)     how many ways to CHOOSE 2 of 5 (order does not matter)
      math.perm(5, 2)     how many ways to ARRANGE 2 of 5 (order matters)
- CONSTANTS: math.pi, math.e, math.tau, math.inf, math.nan.
  math.nan never equals anything, not even itself — test it with math.isnan(x).
- DISTANCE and TRIGONOMETRY:
      math.dist((0, 0), (3, 4))  straight-line distance between two points
      math.hypot(3, 4)           length of the hypotenuse, same 5.0
  The trig functions work in RADIANS, not degrees, so convert first:
      math.radians(180) -> 3.1416...      degrees -> radians
      math.degrees(math.pi / 2) -> 90.0   radians -> degrees
      math.sin(math.radians(30)) -> 0.5
- LOGARITHMS: math.log(x) is the natural log, math.log10(x) and math.log2(x)
  are the base-10 and base-2 versions.
- Floats are approximate, so 0.1 + 0.2 is not exactly 0.3. Compare them with
  math.isclose(a, b) instead of ==, and round only when you PRINT.

Run:  python3 chapters/01_basics/25_math.py
"""

import math
import re


# ---------------------------------------------------------------------------
# Problem 1: Built-ins and the rounding family
# You are given: numbers = [4, -17, 23, 8, -42, 15]
# Use the built-in functions for the first few answers, then the math module
# for the rest. Notice how ceil, floor and round each treat 7.5 differently.
# Return a dict with keys:
#   "smallest"    -> the smallest number in the list
#   "largest"     -> the largest number in the list
#   "total"       -> the sum of the list
#   "abs_min"     -> the smallest number's distance from zero
#   "power"       -> 2 to the power of 10, using pow()
#   "sqrt_144"    -> the square root of 144
#   "ceil_7_2"    -> 7.2 rounded up
#   "floor_7_8"   -> 7.8 rounded down
#   "round_pi"    -> math.pi rounded to 4 decimal places
# (Expected: {'smallest': -42, 'largest': 23, 'total': -9, 'abs_min': 42,
#             'power': 1024, 'sqrt_144': 12.0, 'ceil_7_2': 8, 'floor_7_8': 7,
#             'round_pi': 3.1416})
# ---------------------------------------------------------------------------
def problem_1(numbers=[4, -17, 23, 8, -42, 15]):
    return {
        "smallest": min(numbers),
        "largest": max(numbers),
        "total": sum(numbers),
        "abs_min": abs(min(numbers)),
        "power": pow(2, 10),
        "sqrt_144": math.sqrt(144),
        "ceil_7_2": math.ceil(7.2),
        "floor_7_8": math.floor(7.8),
        "round_pi": round(math.pi, 4),
    }


# ---------------------------------------------------------------------------
# Problem 2: Whole-number maths, and negatives near zero
# Part A — work out factorial(6), gcd(48, 60) and lcm(4, 6).
# Part B — a team of 5 people. How many ways can you CHOOSE 2 of them for a
#   pair (order does not matter), and how many ways can you ARRANGE 2 of them
#   as captain and vice-captain (order matters)? Use math.comb and math.perm.
# Part C — take the whole-number square root of 50 with math.isqrt.
# Part D — apply floor, ceil and trunc to -3.7 and see that they do not agree.
# Return a dict with keys:
#   "factorial", "gcd", "lcm", "choose", "arrange", "isqrt",
#   "floor_neg", "ceil_neg", "trunc_neg"
# (Expected: {'factorial': 720, 'gcd': 12, 'lcm': 12, 'choose': 10,
#             'arrange': 20, 'isqrt': 7, 'floor_neg': -4, 'ceil_neg': -3,
#             'trunc_neg': -3})
# ---------------------------------------------------------------------------
def problem_2():
    return {
        "factorial": math.factorial(6),
        "gcd": math.gcd(48, 60),
        "lcm": math.lcm(4, 6),
        "choose": math.comb(5, 2),
        "arrange": math.perm(5, 2),
        "isqrt": math.isqrt(50),
        "floor_neg": math.floor(-3.7),
        "ceil_neg": math.ceil(-3.7),
        "trunc_neg": math.trunc(-3.7),
    }


# ---------------------------------------------------------------------------
# Problem 3: A geometry report
# Part A — for a circle of radius 5, work out the area (pi * r squared) and the
#   circumference (2 * pi * r). Round both to 2 decimal places.
# Part B — measure the straight-line distance from the point (0, 0) to (3, 4),
#   once with math.dist and once with math.hypot. They must agree.
# Part C — convert 180 degrees into radians (round to 4 places) and pi/2
#   radians into degrees. Then take sin(30 degrees) and cos(60 degrees),
#   rounded to 2 places — remember the trig functions expect RADIANS.
# Part D — take log10(1000) and log2(8).
# Return a dict with keys:
#   "area", "circumference", "dist", "hypot", "radians_180", "degrees_half_pi",
#   "sin_30", "cos_60", "log10", "log2"
# (Expected: {'area': 78.54, 'circumference': 31.42, 'dist': 5.0,
#             'hypot': 5.0, 'radians_180': 3.1416, 'degrees_half_pi': 90.0,
#             'sin_30': 0.5, 'cos_60': 0.5, 'log10': 3.0, 'log2': 3.0})
# ---------------------------------------------------------------------------
def problem_3(radius=5):
    return {
        "area": round(math.pi * radius**2, 2),
        "circumference": round(2 * math.pi * radius, 2),
        "dist": math.dist((0, 0), (3, 4)),
        "hypot": math.hypot(3, 4),
        "radians_180": round(math.radians(180), 4),
        "degrees_half_pi": math.degrees(math.pi / 2),
        "sin_30": round(math.sin(math.radians(30)), 2),
        "cos_60": round(math.cos(math.radians(60)), 2),
        "log10": math.log10(1000),
        "log2": math.log2(8),
    }


if __name__ == "__main__":
    print("Problem 1 (built-ins + rounding):", problem_1())
    print("Problem 2 (whole-number maths):", problem_2())
    print("Problem 3 (geometry report):", problem_3())
