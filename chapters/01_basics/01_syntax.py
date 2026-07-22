"""
Chapter: Python Syntax
======================

Notes
-----
- Python uses INDENTATION (whitespace) to define blocks — not { } braces.
  The standard is 4 spaces per level. Mixing tabs/spaces raises errors.
- A statement normally ends at the end of the line (no semicolon needed).
- Python is CASE SENSITIVE:  name  and  Name  are different variables.
- Comments start with  #.

How to use this file
--------------------
Write your solution inside each problem_N() function so it RETURNS the answer,
then run:   python3 chapters/01_basics/01_syntax.py
Compare the printed output to what each problem asks for.
"""


# ---------------------------------------------------------------------------
# Problem 1: Indentation
# Return the string "positive" when n > 0, otherwise return "non-positive".
# Use an if / else block with correct indentation.
# (Test with n = 7  -> expected "positive")
# ---------------------------------------------------------------------------
def problem_1(n=7):
    if(n > 0) :
        return "positive"
    else:
        return "non-positive"



# ---------------------------------------------------------------------------
# Problem 2: Case sensitivity
# Create two variables named  age  and  Age  with different values,
# and return both as a tuple (age, Age) to prove they are separate names.
# ---------------------------------------------------------------------------
def problem_2():
    age = 5
    Age = 50 
   
    return (age, Age)


# ---------------------------------------------------------------------------
# Problem 3: A nested block
# Using a for-loop with an if-statement inside it, add up only the EVEN
# numbers from 1 to n (inclusive) and return the total.
# (Test with n = 6  -> expected 12, because 2 + 4 + 6 = 12)
# ---------------------------------------------------------------------------
def problem_3(n=6):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i

    return total


if __name__ == "__main__":
    print("Problem 1 (indentation):", problem_1(7))
    print("Problem 2 (case-sensitive):", problem_2())
    print("Problem 3 (nested block):", problem_3())
