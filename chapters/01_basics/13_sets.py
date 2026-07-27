"""
Chapter 13: Python Sets
=======================

Notes
-----
- A set is an UNORDERED collection of UNIQUE items:
      colors = {"red", "green", "red"}      -> {'red', 'green'}
- Because it is unordered there is no indexing: colors[0] raises TypeError.
  Printing a set may show the items in any order — never rely on it.
- Creating sets:
      set()                  the EMPTY set ({} is an empty dict!)
      {1, 2, 3}
      set([1, 1, 2])         -> {1, 2}   (a quick way to drop duplicates)
      {c for c in "hello"}   set comprehension -> {'h', 'e', 'l', 'o'}
- Items must be HASHABLE (immutable): numbers, strings, tuples are fine;
  lists and dicts cannot go in a set.
- Adding / removing:
      s.add(x)               add one item (adding a duplicate does nothing)
      s.update(other)        add every item from another iterable
      s.remove(x)            remove x, KeyError if missing
      s.discard(x)           remove x, silently ignores a missing x
      s.pop()                remove & return an ARBITRARY item
      s.clear()              empty the set
- Set maths — each has an operator and a method:
      a | b   a.union(b)                  in either
      a & b   a.intersection(b)           in both
      a - b   a.difference(b)             in a but not b
      a ^ b   a.symmetric_difference(b)   in exactly one of them
  The operators need both sides to be sets; the methods accept any iterable.
- Relationships:
      a <= b  a.issubset(b)        every item of a is in b
      a >= b  a.issuperset(b)      a contains all of b
      a.isdisjoint(b)              they share nothing
- The *_update methods (intersection_update, difference_update, ...) change the
  set IN PLACE instead of returning a new one.
- Membership testing (x in s) is very fast — much faster than in a long list.
- frozenset(...) is the immutable version; being hashable, it can itself be a
  set member or a dict key.

Run:  python3 chapters/01_basics/13_sets.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Deduplicate while keeping order
# Given a list of items, return a tuple of two things:
#   - a LIST of the distinct items in the order they FIRST appeared
#     (use a set to remember what you have already seen)
#   - the number of duplicates that were dropped
# (Test with ["b", "a", "b", "c", "a", "a"]
#  -> expected (['b', 'a', 'c'], 3))
# ---------------------------------------------------------------------------
import string


def problem_1(items=("b", "a", "b", "c", "a", "a")):
    return (
        set(items),
        len(items) - len(set(items))
    )   



# ---------------------------------------------------------------------------
# Problem 2: Set algebra
# Given two iterables of names, return a dict describing how they overlap:
#     "both"        -> sorted list of names in both
#     "only_first"  -> sorted list of names only in the first
#     "only_second" -> sorted list of names only in the second
#     "either"      -> sorted list of every name
#     "exactly_one" -> sorted list of names in one group but not both
#     "disjoint"    -> True if they share no names at all
# Return sorted lists so the output is predictable.
# (Test with ["ana", "bob", "cid"] and ["bob", "cid", "dee"]
#  -> expected {'both': ['bob', 'cid'], 'only_first': ['ana'],
#               'only_second': ['dee'],
#               'either': ['ana', 'bob', 'cid', 'dee'],
#               'exactly_one': ['ana', 'dee'], 'disjoint': False})
# ---------------------------------------------------------------------------
def problem_2(first=("ana", "bob", "cid"), second=("bob", "cid", "dee")):
    a = set(first)
    b = set(second)
    
    return {
        "both" : sorted(a.intersection(b)),
        "only_first" : sorted(a.difference(b)),
        "only_second" : sorted(b.difference(a)),
        "either" : sorted(a.union(b)),
        "exactly_one" : sorted(a.symmetric_difference(b)),
        "disjoint" : a.isdisjoint(b)
    }


# ---------------------------------------------------------------------------
# Problem 3: Unique letters
# Given a sentence, ignore case and anything that is not a letter, then return
# a dict with:
#     "letters"  -> sorted list of the distinct letters used
#     "count"    -> how many distinct letters that is
#     "missing"  -> sorted list of the a-z letters NOT used
#     "pangram"  -> True if all 26 letters appear
# (Test with "The quick brown fox"
#  -> 'count': 15, 'pangram': False, and 'missing' holds the other 11 letters)
# ---------------------------------------------------------------------------
def problem_3(sentence="The quick brown fox"):
    letters = {c.lower() for c in sentence if c.isalpha()}
    alphabet = set(string.ascii_lowercase)

    return {
        "letters" : letters,
        "count": len(letters),
        "missing": alphabet.difference(letters),
        "pangram": len(alphabet) == len(letters)
    }


if __name__ == "__main__":
    print("Problem 1 (dedupe):", problem_1())
    print("Problem 2 (set algebra):", problem_2())
    print("Problem 3 (unique letters):", problem_3())
