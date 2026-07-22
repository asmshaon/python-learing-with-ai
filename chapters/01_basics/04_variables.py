"""
Chapter 04: Python Variables
============================

Notes
-----
- There is no declaration keyword and no type. A variable is created the moment
  you assign to it:   x = 5
- Python is DYNAMICALLY typed: the same name can be rebound to another type.
      x = 5        # int
      x = "five"   # now a str — perfectly legal
- Naming rules: letters, digits and underscores only; cannot start with a digit;
  case sensitive (age and Age are different); cannot be a reserved keyword
  (if, for, class, None, ...). Convention is snake_case.
- Several names at once:
      a = b = c = 0        # all three point at the same value
      a, b = 1, 2          # tuple unpacking, one name per value
      x, y, z = [1, 2, 3]  # unpacking works on any sequence
  Unpacking is why the idiomatic swap needs no temp variable:  a, b = b, a
- SCOPE: a name assigned inside a function is LOCAL to it and disappears when
  the function returns. Reading an outer name works without ceremony, but
  REBINDING one requires declaring it:
      global name     # rebind a module-level variable
  Without `global`, an assignment inside the function just creates a new local
  that shadows the outer name.

Run:  python3 chapters/01_basics/04_variables.py
"""


counter = 0


# ---------------------------------------------------------------------------
# Problem 1: Swapping without a temp variable
# Swap the two values using tuple unpacking (one line, no third variable)
# and return them as a tuple in their new order.
# (Test with a = 1, b = 2 -> expected (2, 1))
# ---------------------------------------------------------------------------
def problem_1(a=1, b=2):
    a, b = b, a

    return (a, b)


# ---------------------------------------------------------------------------
# Problem 2: Multiple assignment
# Unpack the given list into three separate names in ONE statement,
# then return them as a tuple.
# (Test with [1, 2, 3] -> expected (1, 2, 3))
# ---------------------------------------------------------------------------
def problem_2(values=(1, 2, 3)):
    x, y, z = values

    return (x, y, z)


# ---------------------------------------------------------------------------
# Problem 3: The global keyword
# Increment the module-level  counter  defined above by  step  and return its
# new value. Without `global` you would only create a local copy and the
# module-level counter would stay at 0.
# (Test with step = 5 -> expected 5 on the first call)
# ---------------------------------------------------------------------------
def problem_3(step=5):
    global counter
    counter = counter + step

    return counter


if __name__ == "__main__":
    print("Problem 1 (swap):", problem_1())
    print("Problem 2 (unpacking):", problem_2())
    print("Problem 3 (global):", problem_3())
 