"""
Chapter 03: Python Comments
===========================

Notes
-----
- A comment starts with  #  and runs to the end of the line. Python ignores it
  completely, so it never affects what the code does.
- It can sit on its own line, or INLINE after code:
      total = 0      # start the running sum
- Python has NO /* ... */ block comment. For several lines you stack #, one per
  line. Most editors do this with a keyboard shortcut.
- A bare string literal on its own line is NOT a comment — it is an expression
  that Python evaluates and throws away. It only becomes special in one place:
  as the FIRST statement of a module, function, or class, where it becomes the
  DOCSTRING and is stored on the object's __doc__ attribute.
      module docstring   -> __doc__
      function docstring -> my_function.__doc__
  That is the difference that matters: comments vanish at runtime, docstrings
  are real data you can read back.
- Commenting out a line is the normal way to temporarily disable code while
  testing, instead of deleting it.

Run:  python3 chapters/01_basics/03_comments.py
"""


# ---------------------------------------------------------------------------
# Problem 1: A function docstring
# Give this function a docstring whose text is exactly:  Adds two numbers.
# Then return that docstring by reading it back off the function itself
# (a function's docstring lives on its __doc__ attribute).
# (expected "Adds two numbers.")
# ---------------------------------------------------------------------------

def problem_1():
  """
  Adds two numbers.
  """

  return problem_1.__doc__.strip()


# ---------------------------------------------------------------------------
# Problem 2: Commenting out a line
# The line marked BUG below spoils the total. Disable it with a comment
# (do not delete it) so the function returns the correct sum, then return total.
# (expected 6, because 1 + 2 + 3 = 6)
# ---------------------------------------------------------------------------
def problem_2():
    total = 0
    for i in [1, 2, 3]:
        total += i
        #total += 100  # BUG: comment this line out
    return total


# ---------------------------------------------------------------------------
# Problem 3: The module docstring
# This file's own docstring is the text at the very top, available as __doc__.
# Return just its FIRST line.
# (expected "Chapter 03: Python Comments")
# ---------------------------------------------------------------------------
def problem_3():
    return __doc__.strip().split("\n")[0]


if __name__ == "__main__":
    print("Problem 1 (function docstring):", problem_1())
    print("Problem 2 (commented-out line):", problem_2())
    print("Problem 3 (module docstring):", problem_3())
