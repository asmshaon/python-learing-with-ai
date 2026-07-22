"""
Chapter 05: Python Data Types
=============================

Notes
-----
- Every value in Python is an object, and every object has a TYPE. You never
  declare the type — the value you assign decides it. Ask at runtime with
  type(x), which returns the class itself, so type(5) prints as int.
- The built-in types worth knowing now, grouped by what they are for:
      Text        str                     "hello"
      Numeric     int, float, complex     7, 7.0, 3+2j
      Sequence    list, tuple, range      [1,2], (1,2), range(3)
      Mapping     dict                    {"a": 1}
      Set         set, frozenset          {1,2}, frozenset({1,2})
      Boolean     bool                    True
      Binary      bytes, bytearray        b"abc"
      None        NoneType                None
- MUTABLE vs IMMUTABLE is the distinction that causes the most surprises:
      mutable   -> list, dict, set, bytearray   (can be changed in place)
      immutable -> int, float, str, tuple, frozenset, bytes
  "Changing" a str actually builds a new str; changing a list does not.
- bool is a SUBCLASS of int: True == 1 and False == 0 are both True, and
  isinstance(True, int) is True. This is why sum([True, True, False]) is 2.
- type(x) is exact; isinstance(x, T) also accepts subclasses. Prefer isinstance
  for checks, because it handles inheritance correctly.
      isinstance(x, (int, float))     # accepts a tuple of types
- You can also set the type explicitly by calling the constructor:
      x = str(20)      # "20"
      y = list((1,2))  # [1, 2]

Run:  python3 chapters/01_basics/05_data_types.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Identify the type
# Return the NAME of each value's type as a list of strings, in the same order
# as the values given. A type object stores its own name on __name__, so
# type(5).__name__ is the string "int".
# (Test with [1, 1.5, "hi", True, None, [1], (1,), {1}, {"a": 1}]
#  -> expected ['int', 'float', 'str', 'bool', 'NoneType', 'list', 'tuple',
#               'set', 'dict'])
# ---------------------------------------------------------------------------
from attr import mutable


def problem_1(values=(1, 1.5, "hi", True, None, [1], (1,), {1}, {"a": 1})):
    return [type(value).__name__ for value in values]


# ---------------------------------------------------------------------------
# Problem 2: Mutable or immutable?
# Decide, for each value, whether its type can be changed in place. Return a
# dict mapping the type's NAME to True (mutable) or False (immutable).
# Hint: you do not need to test it empirically — check membership against a set
# of the mutable type names you know.
# (Test with [[1], (1,), {1}, "hi", {"a": 1}, 5]
#  -> expected {'list': True, 'tuple': False, 'set': True, 'str': False,
#               'dict': True, 'int': False})
# ---------------------------------------------------------------------------
def problem_2(values=([1], (1,), {1}, "hi", {"a": 1}, 5)):
    miDic = {}

    for value in values:
        miDic.items({type(value).__name__ : value.mutable})
    
    return miDic


# ---------------------------------------------------------------------------
# Problem 3: type() vs isinstance() on bool
# Because bool subclasses int, the two checks disagree for True. Return a tuple
# of four booleans, in this order:
#     type(True) is int          -> exact type match, so False
#     isinstance(True, int)      -> subclass counts, so True
#     type(True) is bool         -> True
#     isinstance(True, bool)     -> True
# (expected (False, True, True, True))
# ---------------------------------------------------------------------------
def problem_3(value=True):
    # your solution here
    pass


if __name__ == "__main__":
    print("Problem 1 (type names):", problem_1())
    print("Problem 2 (mutability):", problem_2())
    print("Problem 3 (type vs isinstance):", problem_3())
