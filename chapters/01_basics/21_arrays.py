"""
Chapter 21: Python Arrays
=========================

Notes
-----
- Python has no built-in array TYPE the way C or Java do. In everyday Python the
  "array" of the tutorials is just a LIST — it holds a sequence of items you
  reach by index, and it can mix types.
- Index and length:
      cars = ["ford", "bmw", "kia"]
      cars[0]        first item
      cars[-1]       last item
      len(cars)      how many items
  Indexes run 0 .. len-1; anything outside that raises IndexError.
- Looping over an array: `for car in cars` gives items, enumerate() gives index
  and item together. `for i in range(len(cars))` is the index-only version.
- The methods you use on an array-as-list:
      append(x)      add one item at the end
      extend(other)  add every item of another iterable
      insert(i, x)   put x at index i, shifting the rest right
      remove(x)      delete the FIRST item equal to x (ValueError if absent)
      pop(i)         remove AND return the item at i (last one if i is left out)
      clear()        empty it
      index(x)       position of the first x
      count(x)       how many times x appears
      sort()         sort IN PLACE (returns None) — sorted() returns a new list
      reverse()      reverse in place
      copy()         a new list with the same items
- A list is MUTABLE and assignment does not copy it: `b = a` makes b another
  name for the SAME list, so changing b changes a. Use a.copy() or a[:] for a
  separate list.
- SLICING reads a section and gives a NEW list: items[1:4], items[:3],
  items[-2:], items[::2], items[::-1] (reversed copy). Slice assignment can
  replace a whole section at once.
- A 2D array is a list of lists; grid[row][col] reaches one cell. Build one with
  a comprehension — [[0] * cols for _ in range(rows)]. Do NOT write
  [[0] * cols] * rows: that repeats the SAME inner list, so writing one row
  writes them all.
- When you want a real fixed-type array, the standard library has the array
  module — array("i", [1, 2, 3]) stores machine integers only and is compact.
  For numeric work with maths on whole arrays at once, NumPy is the real tool
  (that is section 04).

Run:  python3 chapters/01_basics/21_arrays.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Walk an array by index and by item
# Given an array of temperatures, return a dict with:
#   "length"   -> how many readings there are
#   "first"    -> the first reading
#   "last"     -> the last reading, found WITHOUT using len()
#   "highest"  -> the largest reading, found with your own loop (no max())
#   "average"  -> the mean, rounded to 1 decimal place
#   "above"    -> a list of the readings above the average
#   "indexed"  -> a list of "i:value" strings using enumerate, e.g. "0:21.5"
# (Test with [21.5, 19.0, 24.5, 22.0]
#  -> expected {'length': 4, 'first': 21.5, 'last': 22.0, 'highest': 24.5,
#               'average': 21.8, 'above': [24.5, 22.0],
#               'indexed': ['0:21.5', '1:19.0', '2:24.5', '3:22.0']})
# ---------------------------------------------------------------------------
def problem_1(readings=(21.5, 19.0, 24.5, 22.0)):
    # TODO: your solution here
    pass


# ---------------------------------------------------------------------------
# Problem 2: Modifying an array, and the aliasing trap
# Start from the array ["ford", "bmw", "kia"]. Make a COPY to work on, then on
# that copy: append "audi", insert "opel" at index 1, remove "bmw", and pop the
# last item (keep what pop gave you). Finally sort it.
# Also show the trap: make an ALIAS of the original (plain assignment), append
# "tesla" through the alias, and report whether the original changed.
# Return a dict with keys:
#   "changed"  -> the sorted working copy
#   "popped"   -> the item pop() returned
#   "original" -> the original array after the alias was modified
#   "aliased"  -> True if the alias and the original are the same object
# (Expected: {'changed': ['ford', 'opel'], 'popped': 'audi',
#             'original': ['ford', 'bmw', 'kia', 'tesla'], 'aliased': True})
# ---------------------------------------------------------------------------
def problem_2():
    # TODO: your solution here
    pass


# ---------------------------------------------------------------------------
# Problem 3: Slices and a 2D array
# Part A — from the array [10, 20, 30, 40, 50, 60], use slices only to get:
#   "head" -> the first three, "tail" -> the last two,
#   "evens_pos" -> every second item starting at index 0,
#   "backwards" -> the whole array reversed as a NEW list.
# Part B — build a rows x cols grid of zeros the SAFE way, then write the value
#   row * cols + col into every cell. Return it as "grid", plus "row_sums" (the
#   total of each row) and "column" (column 0 as a flat list).
# Return one dict with all seven keys.
# (Test with rows=3, cols=2
#  -> grid [[0, 1], [2, 3], [4, 5]], row_sums [1, 5, 9], column [0, 2, 4])
# ---------------------------------------------------------------------------
def problem_3(numbers=(10, 20, 30, 40, 50, 60), rows=3, cols=2):
    # TODO: your solution here
    pass


if __name__ == "__main__":
    print("Problem 1 (walking an array):", problem_1())
    print("Problem 2 (modify + aliasing):", problem_2())
    print("Problem 3 (slices + 2D):", problem_3())
