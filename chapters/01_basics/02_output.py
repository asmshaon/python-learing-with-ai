"""
Chapter 02: Python Output
=========================

Notes
-----
- print() is a FUNCTION, so it always needs parentheses:  print("hi")
- It accepts many arguments at once and joins them with a space by default:
      print("a", "b")        ->  a b
- Two keyword arguments control the formatting:
      sep=  what goes BETWEEN the arguments   (default a single space " ")
      end=  what goes AFTER the last one      (default a newline "\\n")
  So  print("a", "b", sep="-", end="!")  prints  a-b!  with no line break.
- print() DISPLAYS a value and returns None. That is why the problems in this
  repo must `return` their answer — printing alone leaves the function
  returning None and nothing can be tested.
- print() calls str() on each argument for you, so numbers need no conversion.
  But building a string yourself DOES need it:  "Age: " + str(30).
- "\\n" inside a string is a newline; "\\t" is a tab.

Run:  python3 chapters/01_basics/02_output.py
"""


# ---------------------------------------------------------------------------
# Problem 1: The sep argument
# print("a", "b", "c", sep="-")  displays a single line of text.
# Return that exact line as a string (do not print it).
# (expected "a-b-c")
# ---------------------------------------------------------------------------
def problem_1():
    return "-".join(["a", "b", "c"])


# ---------------------------------------------------------------------------
# Problem 2: The end argument
# Printing a list with end="" puts every item on ONE line instead of
# one per line. Build that single line from the given list and return it.
# (Test with ["x", "y", "z"] -> expected "x y z")
# ---------------------------------------------------------------------------
def problem_2(items=("x", "y", "z")):
    return " ".join(items)


# ---------------------------------------------------------------------------
# Problem 3: Mixing text and numbers
# Combine a label and a number into one output line and return it.
# Remember a number must be converted before it can be joined to a string.
# (Test with "Age", 30 -> expected "Age: 30")
# ---------------------------------------------------------------------------
def problem_3(label="Age", value=30):
    return f"{label}: {str(value)}"


if __name__ == "__main__":
    print("Problem 1 (sep):", problem_1())
    print("Problem 2 (end):", problem_2())
    print("Problem 3 (text + number):", problem_3())


for x in range(2, 30, 3):
    print(x)
