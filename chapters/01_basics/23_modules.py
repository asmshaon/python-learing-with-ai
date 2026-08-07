"""
Chapter 23: Python Modules
==========================

Notes
-----
- A MODULE is simply a .py file. The moment you write helpers into their own
  file you have made a module, and any other file can import it. A PACKAGE is a
  folder of modules.
- The four ways to import:
      import math                  the whole module, used as math.sqrt(9)
      import math as m             the same thing under a shorter ALIAS
      from math import sqrt, pi    pull single names straight into your file
      from math import sqrt as s   a name, renamed
  Avoid `from math import *` — it dumps every name into your file and you can no
  longer tell where something came from.
- Importing runs the file ONCE. Python caches it in sys.modules, so a second
  import of the same module is free and does not re-run the code.
- Every module carries attributes about itself:
      __name__   its name as a string ("math")
      __doc__    its docstring
      __file__   the path it was loaded from (built-ins may not have one)
  dir(module) lists every name the module contains, which is the quickest way to
  explore an unfamiliar library.
- __name__ is the trick behind the block at the bottom of every chapter here.
  When a file is RUN directly its __name__ is the string "__main__"; when the
  same file is IMPORTED its __name__ is the module name instead. That is why
  `if __name__ == "__main__":` runs the demo only when you run the file.
- importlib.import_module("string") imports by NAME given as a string — useful
  when the module you want is decided while the program is running.
- getattr(module, "name") reaches an attribute whose name is in a variable, and
  hasattr(module, "name") checks whether it exists.
- Standard library modules worth knowing early: math, random, datetime, json,
  os, sys, statistics, string, itertools, re.
- random is PSEUDO-random: seed it with random.seed(42) and it produces the same
  sequence every run, which is what makes a random program testable.

Run:  python3 chapters/01_basics/23_modules.py
"""

import math as m
import string
from importlib import import_module
from pathlib import Path
from random import choice, randint, seed


# ---------------------------------------------------------------------------
# Problem 1: Import a module and use it through an alias
# Using the math module imported ABOVE as `m`, return a dict with keys:
#   "pi"          -> pi rounded to 4 decimal places
#   "sqrt"        -> the square root of 144
#   "factorial"   -> 5 factorial
#   "ceil"        -> 4.2 rounded UP
#   "floor"       -> 4.8 rounded DOWN
#   "module_name" -> the module's own __name__ attribute
#   "has_sqrt"    -> True if "sqrt" appears in dir(m)
# (Expected: {'pi': 3.1416, 'sqrt': 12.0, 'factorial': 120, 'ceil': 5,
#             'floor': 4, 'module_name': 'math', 'has_sqrt': True})
# ---------------------------------------------------------------------------
def problem_1():
    return {
        "pi": round(m.pi, 4),
        "sqrt": m.sqrt(144),
        "factorial": m.factorial(5),
        "ceil": m.ceil(4.2),
        "floor": m.floor(4.8),
        "module_name": m.__name__,
        "has_sqrt": "sqrt" in dir(m),
    }


# ---------------------------------------------------------------------------
# Problem 2: from-imports and a seeded random module
# seed, randint and choice were imported by NAME above, so call them directly
# (no "random." prefix).
# Seed with the given number, then build a list of three randint(1, 100) values
# and pick one choice() from ["red", "green", "blue"]. Now seed with the SAME
# number again and repeat exactly the same calls.
# Return a dict with keys:
#   "first_run"   -> [three numbers, then the colour]  (4 items in total)
#   "second_run"  -> the same four things, generated again after re-seeding
#   "repeatable"  -> True if the two runs are equal
#   "in_range"    -> True if every number is between 1 and 100
# (Do not hard-code the numbers — the point is that seeding makes the two runs
#  identical, so "repeatable" must come out True every single time you run it.)
# ---------------------------------------------------------------------------
def problem_2(seed_value=42):
    seed(seed_value)
    colors = ["red", "green", "blue"]

    first_run = [randint(1, 100) for _ in range(3)]
    first_run.append(choice(colors))

    seed(seed_value)

    second_run = [randint(1, 100) for _ in range(3)]
    second_run.append(choice(colors))

    return {
        "first_run": first_run,
        "second_run": second_run,
        "repeatable": first_run == second_run,
        "in_range": all(1 <= n <= 100 for n in first_run[:3]),
    }


# ---------------------------------------------------------------------------
# Problem 3: Inspect a module, and inspect THIS file
# Part A — import the string module BY NAME using import_module("string"), then
#   describe it: its __name__, its `digits` constant, how many letters are in
#   `ascii_lowercase`, and whether it has a `capwords` attribute (use hasattr).
#   Reach the digits value with getattr(mod, "digits") rather than a dot.
# Part B — report this chapter file's own __name__. Because you are running the
#   file directly it is the string "__main__"; if another file imported this one
#   it would read "23_modules" instead.
# Part C — confirm that importing the same module twice gives the SAME object
#   (compare the module you imported at the top with the one import_module gave
#   you, using `is`).
# Return a dict with keys:
#   "module_name", "digits", "lowercase_len", "has_capwords", "this_module",
#   "cached"
# (Expected: {'module_name': 'string', 'digits': '0123456789',
#             'lowercase_len': 26, 'has_capwords': True,
#             'this_module': '__main__', 'cached': True})
# ---------------------------------------------------------------------------
def problem_3():
    str = import_module("string")

    return {
        "module_name": str.__name__,
        "digits": getattr(str, "digits"),
        "lowercase_len": len(str.ascii_lowercase),
        "has_capwords": hasattr(str, "capwords"),
        "this_module": __name__,
        "cached": str is string,
    }


if __name__ == "__main__":
    print("Problem 1 (math via alias):", problem_1())
    print("Problem 2 (from-import + seed):", problem_2())
    print("Problem 3 (inspecting modules):", problem_3())
