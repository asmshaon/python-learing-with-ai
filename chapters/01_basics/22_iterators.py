"""
Chapter 22: Python Iterators
============================

Notes
-----
- Two words that sound the same but are not:
      ITERABLE  — something you CAN loop over (list, tuple, string, dict, set,
                  range, file). It knows how to hand out an iterator.
      ITERATOR  — the thing doing the walking. It remembers WHERE it is and
                  gives you the next item when asked.
- The protocol is two dunder methods:
      __iter__()  returns an iterator (on an iterator itself, it returns self)
      __next__()  returns the next item, or raises StopIteration when finished
  The built-ins iter(x) and next(x) call those two for you.
- A for loop is just this loop written for you:
      it = iter(items)
      while True:
          try:
              item = next(it)
          except StopIteration:
              break
          ...body...
  So StopIteration is not an error to fear — it is the normal "I am done" signal
  and the for loop swallows it.
- An iterator is used up ONCE. After it raises StopIteration it stays empty, so
  looping a second time over the SAME iterator gives you nothing. A list is
  reusable because each new for loop asks it for a FRESH iterator.
- next(it, default) returns the default instead of raising when exhausted.
- Writing your own iterator class means writing __iter__ (usually `return self`)
  and __next__ (return the next value, or `raise StopIteration`).
- A GENERATOR is the short way to write an iterator. Any function containing
  `yield` returns a generator when called; each yield hands back one value and
  freezes the function until the next call resumes it.
- A GENERATOR EXPRESSION looks like a list comprehension with round brackets:
      (n * n for n in range(5))
  It builds nothing up front — values appear one at a time. That is LAZY
  evaluation, and it is why a generator can describe an INFINITE sequence
  without running out of memory.
- The itertools module is a toolbox of ready-made iterators. count(start, step)
  counts forever, islice(it, n) takes the first n items, cycle() repeats.

Run:  python3 chapters/01_basics/22_iterators.py
"""

from itertools import count, islice


# ---------------------------------------------------------------------------
# Problem 1: Drive an iterator by hand
# Given the tuple ("a", "b", "c", "d"), do NOT use a for loop. Instead get an
# iterator with iter(), pull the first two items with next(), then collect the
# REST inside a while loop that catches StopIteration to stop. Finally call
# next() one more time on the finished iterator and report that it is empty.
# Return a dict with keys:
#   "first"       -> the first item pulled
#   "second"      -> the second item pulled
#   "rest"        -> a list of everything the while loop collected
#   "exhausted"   -> True if a further next() raised StopIteration
#   "self_iter"   -> True if iter(it) is the very same iterator object
#   "tuple_has_next" -> whether the ORIGINAL tuple has a __next__ method
# (Expected: {'first': 'a', 'second': 'b', 'rest': ['c', 'd'],
#             'exhausted': True, 'self_iter': True, 'tuple_has_next': False})
# ---------------------------------------------------------------------------
def problem_1(data=("a", "b", "c", "d")):

    it = iter(data)
    first = next(it)
    second = next(it)
    rest = []
    exhausted = False

    while True:
        try:
            rest.append(next(it))
        except StopIteration:
            break

    try:
        next(it)
    except StopIteration:
        exhausted = True

    return {
        "first": first,
        "second": second,
        "rest": rest,
        "exhausted": exhausted,
        "self_iter": iter(it) == it,
        "tuple_has_next": hasattr(data, "__next__"),
    }


# ---------------------------------------------------------------------------
# Problem 2: Write your own iterator class
# Build a class Countdown that counts DOWN from a starting number to 1.
#   Countdown(5) looped over should give 5, 4, 3, 2, 1 and then stop.
# Give it __iter__ (returning self) and __next__ (raising StopIteration once it
# has passed 1).
# Then prove the "used up once" rule: make ONE Countdown(5) object, turn it into
# a list, then turn the SAME object into a list again — the second time must be
# empty. Show that a brand new Countdown(3) still works.
# Return a dict with keys:
#   "first_pass"  -> list from the first walk
#   "second_pass" -> list from walking the same object again
#   "fresh"       -> list from a new Countdown(3)
#   "is_iterator" -> True if the object has both __iter__ and __next__
# (Expected: {'first_pass': [5, 4, 3, 2, 1], 'second_pass': [],
#             'fresh': [3, 2, 1], 'is_iterator': True})
# ---------------------------------------------------------------------------
def problem_2(start=5):
    countdown = Countdown(5)
    countdown_fresh = Countdown(3)

    return {
        "first_pass": list(countdown),
        "second_pass": list(countdown),
        "fresh": list(countdown_fresh),
        "is_iterator": hasattr(countdown, "__iter__")
        and hasattr(countdown, "__next__"),
    }


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration

        value = self.current
        self.current -= 1

        return value


# ---------------------------------------------------------------------------
# Problem 3: Generators and laziness
# Part A — write a generator function fib() that yields Fibonacci numbers
#   FOREVER (0, 1, 1, 2, 3, 5, ...). Take only the first 8 of them.
# Part B — use a GENERATOR EXPRESSION to add up the squares of 1..5, and report
#   the type name of that expression object before it is consumed.
# Part C — use itertools.count(10, 5) with islice to take 4 values from an
#   infinite counter.
# Return a dict with keys:
#   "fib"         -> the first 8 Fibonacci numbers as a list
#   "squares_sum" -> the sum of the squares of 1..5
#   "lazy"        -> type(...).__name__ of the generator expression
#   "sliced"      -> the 4 values taken from count(10, 5)
# (Expected: {'fib': [0, 1, 1, 2, 3, 5, 8, 13], 'squares_sum': 55,
#             'lazy': 'generator', 'sliced': [10, 15, 20, 25]})
# ---------------------------------------------------------------------------
from itertools import count, islice


def problem_3(how_many=8):
    fib = fibonacci()

    gen = (n * n for n in range(1, 6))

    return {
        "fib": list(islice(fib, how_many)),
        "squares_sum": sum(gen),
        "lazy": type(gen).__name__,
        "sliced": list(islice(count(10, 5), 4)),
    }


def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("Problem 1 (iterator by hand):", problem_1())
    print("Problem 2 (custom iterator):", problem_2())
    print("Problem 3 (generators):", problem_3())
