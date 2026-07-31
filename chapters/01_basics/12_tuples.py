"""
Chapter 12: Python Tuples
=========================

Notes
-----
- A tuple is an ORDERED, IMMUTABLE collection that allows duplicates:
      point = (3, 7)
      colors = ("red", "green", "red")
- Immutable means no append / remove / item assignment:
      point[0] = 9      -> TypeError
  To "change" a tuple, convert to a list, edit, convert back:
      tmp = list(point); tmp[0] = 9; point = tuple(tmp)
- Creating tuples:
      ()                    empty tuple
      (42,)                 ONE item needs the trailing comma
      (42)                  is just the int 42 — not a tuple!
      1, 2, 3               parentheses are optional
      tuple("abc")          -> ('a', 'b', 'c')
- Indexing and slicing work exactly like lists (read-only):
      colors[0]  colors[-1]  colors[1:3]  colors[::-1]
- Unpacking assigns items to names in one line:
      x, y = point
      first, *rest = (1, 2, 3, 4)      -> first=1, rest=[2, 3, 4]
      a, b = b, a                      -> swap without a temp variable
  The star (*) collects the leftover items into a LIST.
- Joining / repeating make NEW tuples:
      (1, 2) + (3,)        -> (1, 2, 3)
      ("ab",) * 3          -> ('ab', 'ab', 'ab')
- Only two tuple methods exist:  t.count(x)  and  t.index(x).
  The generic helpers still apply: len, sum, min, max, sorted, x in t.
- sorted(t) returns a LIST, not a tuple — wrap it in tuple() if you need one.
- Why tuples? They signal "this must not change", they are slightly faster and
  smaller than lists, and because they are hashable they can be dict keys or
  set members (a list cannot).
- Functions returning several values are really returning a tuple:
      def stats(): return 1, 2      ->  (1, 2)

Run:  python3 chapters/01_basics/12_tuples.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Tuple basics and the one-item trap
# Build and return a tuple of four items, in this order:
#   - a tuple holding only the number 42 (a real 1-item tuple)
#   - the type of the expression (42) written without a trailing comma
#   - the tuple ("a", "b") joined with ("c",)
#   - the tuple ("hi",) repeated 3 times
# (Expected (42,), <class 'int'>, ('a', 'b', 'c'), ('hi', 'hi', 'hi'))
# ---------------------------------------------------------------------------
from pyparsing import Word


def problem_1():
    return (
        (42,),
        type((42)),
        (
            "a",
            "b",
        )
        + ("c",),
        ("hi",) * 3,
    )


# ---------------------------------------------------------------------------
# Problem 2: Unpacking
# Given a tuple of at least 3 numbers, return a dict with:
#     "first"   -> the first item
#     "last"    -> the last item
#     "middle"  -> a LIST of everything between first and last (use star unpacking)
#     "swapped" -> a 2-tuple of (last, first)
# Do all of it with unpacking, not with indexing.
# (Test with (10, 20, 30, 40)
#  -> expected {'first': 10, 'last': 40, 'middle': [20, 30],
#               'swapped': (40, 10)})
# ---------------------------------------------------------------------------
def problem_2(values=(10, 20, 30, 40)):
    first, *middle, last = values

    return {"first": first, "last": last, "middle": middle, "swapped": (last, first)}


# ---------------------------------------------------------------------------
# Problem 3: Working around immutability
# Given a tuple of words, return a tuple of three NEW tuples:
#   - the same words sorted alphabetically (as a tuple, not a list)
#   - the words with every occurrence of "red" removed
#   - the words with "blue" added at index 1
# The input tuple must still be unchanged when you are done.
# (Test with ("red", "green", "red", "yellow")
#  -> expected (('green', 'red', 'red', 'yellow'),
#               ('green', 'yellow'),
#               ('red', 'blue', 'green', 'red', 'yellow')))
# ---------------------------------------------------------------------------
def problem_3(words=("red", "green", "red", "yellow")):
    words_list = list(words)
    words_list.insert(1, "blue")

    return (
        sorted(words),
        tuple(word for word in words if word != "red"),
        tuple(words_list),
    )


if __name__ == "__main__":
    print("Problem 1 (tuple basics):", problem_1())
    print("Problem 2 (unpacking):", problem_2())
    print("Problem 3 (immutability):", problem_3())
