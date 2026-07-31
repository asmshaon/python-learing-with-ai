"""
Chapter 20: Python Range
========================

Notes
-----
- range() produces a sequence of whole numbers. Three forms:
      range(stop)               0 .. stop-1
      range(start, stop)        start .. stop-1
      range(start, stop, step)  start, start+step, ... while below stop
  The stop value is ALWAYS excluded. Only integers are allowed — no floats.
- range is LAZY: it is not a list. It stores start/stop/step and computes values
  as you ask for them, so range(1_000_000) costs almost no memory. Wrap it in
  list() when you actually want the numbers:
      list(range(1, 6))  ->  [1, 2, 3, 4, 5]
- A negative step counts DOWN. Then start must be higher than stop:
      range(10, 0, -2)  ->  10, 8, 6, 4, 2
  step of 0 is an error.
- An empty range is not an error, it just yields nothing — range(5, 5),
  range(5, 1), range(1, 5, -1) are all empty.
- Because it is a real sequence you can index, slice, and reverse it, and it
  supports len() and the in operator:
      r = range(0, 20, 5)
      r[2]        -> 10
      len(r)      -> 4
      15 in r     -> True      (this check is fast, it does no scanning)
      r[::-1]     -> range(15, -5, -5)
  reversed(range(5)) walks 4,3,2,1,0.
- Number of items in a range, without building it:
      len(range(start, stop, step))
- Common pairings:
      for i in range(len(items))          works, but enumerate() is usually better
      for _ in range(n)                   just repeat n times, value unused
      sum(range(1, 101))                  5050, no loop needed
      [x * x for x in range(1, 6)]        build a list from a range
- range only does integers, so for fractional steps compute from an int range:
      [i / 10 for i in range(0, 11)]      0.0 .. 1.0 in steps of 0.1

Run:  python3 chapters/01_basics/20_range.py
"""


# ---------------------------------------------------------------------------
# Problem 1: The three forms, forwards and backwards
# Return a dict of lists built from range only (use list() to materialise them):
#   "count"     -> 0 to 4
#   "from_one"  -> 1 to 10
#   "odds"      -> odd numbers below 10, using a step
#   "countdown" -> 10 down to 1
#   "empty"     -> a range that yields nothing, as a list
# (Expected: {'count': [0, 1, 2, 3, 4], 'from_one': [1, 2, ..., 10],
#             'odds': [1, 3, 5, 7, 9], 'countdown': [10, 9, ..., 1],
#             'empty': []})
# ---------------------------------------------------------------------------
def problem_1():
    return {
        "count": list(range(5)),
        "from_one": list(range(1, 11)),
        "odds": [n for n in range(1, 10, 2)],
        "countdown": [n for n in range(10, 0, -1)],
        "empty": list(range(5, 5)),
    }


# ---------------------------------------------------------------------------
# Problem 2: range as a sequence — no loops allowed
# Given start, stop and step, build the range ONCE and answer these questions
# about it WITHOUT writing a for/while loop and without calling list():
#   "length"   -> how many numbers it holds
#   "first"    -> its first value
#   "last"     -> its last value (index from the end)
#   "third"    -> the value at index 2
#   "has_stop" -> is the stop value itself a member?
#   "middle"   -> the middle third of it, as a list (use a slice, then list())
# Return them as a dict.
# (Test with start=0, stop=30, step=3
#  -> expected {'length': 10, 'first': 0, 'last': 27, 'third': 6,
#               'has_stop': False, 'middle': [9, 12, 15]})
# ---------------------------------------------------------------------------
def problem_2(start=0, stop=30, step=3):
    my_range = range(start, stop, step)
    n = len(my_range)

    return {
        "length": len(my_range),
        "first": my_range[0],
        "last": my_range[len(my_range) - 1],
        "third": my_range[2],
        "has_stop": stop in my_range,
        "middle": list(my_range[n // 3 : 2 * n // 3]),
    }


# ---------------------------------------------------------------------------
# Problem 3: Ranges in real use
# Return a dict with:
#   "sum_evens"  -> the sum of all even numbers from 1 to 100 inclusive, built
#                   with a single range and sum() (no loop, no if)
#   "squares"    -> a list of the squares of 1..10, via a comprehension
#   "fizzbuzz"   -> for 1..15, a list where each item is "fizz" if divisible by
#                   3, "buzz" if by 5, "fizzbuzz" if by both, else the number
#                   itself as an int
#   "decimals"   -> [0.0, 0.25, 0.5, 0.75, 1.0] — range only makes integers, so
#                   derive these from an int range
#   "chunks"     -> [1..10] split into groups of 3, as a list of lists, using a
#                   range with a step to pick the slice starting points
#                   -> [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
# ---------------------------------------------------------------------------
def problem_3():
    return {
        "sum_evens": sum(range(2, 101, 2)),
        "squares": [n * n for n in range(1, 11)],
        "fizzbuzz": [
            (
                "fizzbuzz"
                if n % 15 == 0
                else "fizz" if n % 3 == 0 else "buzz" if n % 5 == 0 else n
            )
            for n in range(1, 16)
        ],
        "decimals": [i / 4 for i in range(0, 5)],
        "chunks": [list(range(i, i + 3 if i < 10 else i + 1)) for i in range(1, 11, 3)],
    }


if __name__ == "__main__":
    print("Problem 1 (range forms):", problem_1())
    print("Problem 2 (range as sequence):", problem_2())
    print("Problem 3 (ranges in use):", problem_3())
