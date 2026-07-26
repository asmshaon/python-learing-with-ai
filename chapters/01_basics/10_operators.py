"""
Chapter 10: Python Operators
============================

Notes
-----
- Arithmetic:
      +  -  *  /        /  is TRUE division and always gives a float (7/2 -> 3.5)
      //                floor division, rounds toward -inf (7//2 -> 3, -7//2 -> -4)
      %                 modulo / remainder (7 % 3 -> 1); great for even/odd
      **                power (2 ** 10 -> 1024)
- Assignment shortcuts combine an operation with =:
      x += 1   x -= 2   x *= 3   x //= 2   x %= 5   x **= 2 ...
- Comparison operators return a bool:  ==  !=  <  >  <=  >=
  They can be CHAINED like math:  0 < x < 10  means  (0 < x) and (x < 10).
- Logical:  and  or  not   (see the Booleans chapter for short-circuiting).
- Identity vs equality:
      ==   compares VALUES        [1,2] == [1,2]  -> True
      is   compares IDENTITY      whether they are the SAME object in memory
  Use `is` only for singletons like None:  `if x is None`.
- Membership:  x in container   /   x not in container.
- Bitwise (operate on the binary digits of ints):
      &  AND   |  OR   ^  XOR   ~  NOT   <<  left shift   >>  right shift
      5 & 3 -> 1,  5 | 3 -> 7,  5 ^ 3 -> 6,  1 << 4 -> 16
- Precedence (high -> low), when in doubt add parentheses:
      **  ->  unary -/~  ->  * / // %  ->  + -  ->  comparisons  ->
      not  ->  and  ->  or

Run:  python3 chapters/01_basics/10_operators.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Arithmetic breakdown
# Given two integers a and b, return a dict of every arithmetic result:
#     "sum", "difference", "product", "true_div", "floor_div",
#     "remainder", "power"
# (Test with a=17, b=5
#  -> expected {'sum': 22, 'difference': 12, 'product': 85,
#               'true_div': 3.4, 'floor_div': 3, 'remainder': 2, 'power': 1419857})
# ---------------------------------------------------------------------------
def problem_1(a=17, b=5):
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "true_div": a / b,
        "floor_div": a // b,
        "remainder": a % b,
        "power": a ** b,
    }


# ---------------------------------------------------------------------------
# Problem 2: Split seconds into h:m:s using // and %
# Given a total number of seconds, break it into whole hours, minutes, and
# seconds and return them as a tuple (hours, minutes, seconds).
# (Test with 3661 -> expected (1, 1, 1); 7325 -> (2, 2, 5))
# ---------------------------------------------------------------------------
def problem_2(total_seconds=3661):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return (hours, minutes, seconds)


# ---------------------------------------------------------------------------
# Problem 3: Comparison and logic checks
# Given a number, return a dict of boolean facts about it:
#     "in_range"    True if 0 <= n <= 100          (chained comparison)
#     "is_even"     True if n is even
#     "sign"        "positive", "negative", or "zero"
#     "is_none"     whether n is None              (identity check with `is`)
# (Test with 42 -> expected {'in_range': True, 'is_even': True,
#                            'sign': 'positive', 'is_none': False})
# ---------------------------------------------------------------------------
def problem_3(n=42):
    return {
        "in_range": 0 <= n <= 100,
        "is_even":n % 2 == 0,
        "sign": 'positive' if n > 0 else 'nevetive',
        "is_none": n is None,
    }


if __name__ == "__main__":
    print("Problem 1 (arithmetic):", problem_1())
    print("Problem 2 (h:m:s):", problem_2())
    print("Problem 3 (comparison/logic):", problem_3())
