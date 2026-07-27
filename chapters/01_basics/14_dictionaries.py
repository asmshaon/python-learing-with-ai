"""
Chapter 14: Python Dictionaries
===============================

Notes
-----
- A dict stores KEY -> VALUE pairs. Keys are unique and hashable, values can be
  anything:
      person = {"name": "Ana", "age": 30}
- Since Python 3.7 a dict keeps its INSERTION order.
- Creating dicts:
      {}                              empty dict
      dict(name="Ana", age=30)        keyword form (keys must be identifiers)
      dict([("a", 1), ("b", 2)])      from pairs
      dict.fromkeys(["a", "b"], 0)    -> {'a': 0, 'b': 0}
      {c: ord(c) for c in "abc"}      dict comprehension
- Reading values:
      person["name"]          KeyError if the key is missing
      person.get("email")     returns None instead of raising
      person.get("email", "-")  returns the fallback "-" instead
- Writing values:
      person["city"] = "Dhaka"        adds or overwrites
      person.setdefault("tags", [])   returns the value, inserting it only if
                                      the key was missing
      person.update({"age": 31})      merge another dict / pairs in
      a | b                           NEW merged dict (b wins on conflicts)
- Removing:
      person.pop("age")               remove & RETURN the value
      person.pop("nope", None)        with a fallback, no KeyError
      person.popitem()                remove & return the LAST pair
      del person["name"]
      person.clear()
- Views — they stay in sync with the dict:
      person.keys()  person.values()  person.items()
  Looping:
      for key in person: ...
      for key, value in person.items(): ...
- "key in person" tests KEYS, not values. Use "v in person.values()" for values.
- Nesting is common — a dict of dicts, or a dict of lists:
      grades = {"ana": [90, 80], "bob": [70]}
      grades["ana"][0]      -> 90
- Careful: b = a does NOT copy. Use a.copy() or dict(a) for a shallow copy
  (nested objects are still shared); copy.deepcopy(a) for a full copy.

Run:  python3 chapters/01_basics/14_dictionaries.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Safe reads and writes
# Start from a copy of the given dict, then:
#   - add the key "city" with value "Dhaka"
#   - overwrite "age" with 31
#   - remove "email" if it is there (no error if it is not)
#   - look up "phone" without raising, falling back to "unknown"
# Return a 2-tuple of (the updated dict, the phone fallback value).
# Do NOT mutate the caller's original dict.
# (Test with {"name": "Ana", "age": 30}
#  -> expected ({'name': 'Ana', 'age': 31, 'city': 'Dhaka'}, 'unknown'))
# ---------------------------------------------------------------------------
from copy import copy
from itertools import count
import statistics


def problem_1(person = {"name": "Ana", "age": 30}):
    copy_person = copy(person)

    copy_person['city'] = 'Dhaka'
    copy_person.update({"age" : 31})
    copy_person.pop("email", None)

    return (copy_person, copy_person.get("phone", "unknown"))

    

# ---------------------------------------------------------------------------
# Problem 2: Counting and inverting
# Given a sentence, split it into lowercase words and return a dict with:
#     "counts"     -> dict mapping each word to how many times it appears
#     "most_common"-> the word with the highest count (any of the ties is fine)
#     "by_count"   -> dict mapping a count to the sorted list of words with it
#     "singles"    -> sorted list of words that appear exactly once
# Build the counts yourself with get() or setdefault() — no collections import.
# (Test with "the cat and the hat and the bat"
#  -> counts {'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1},
#     most_common 'the', by_count {3: ['the'], 1: ['bat', 'cat', 'hat'],
#     2: ['and']}, singles ['bat', 'cat', 'hat'])
# ---------------------------------------------------------------------------
def problem_2(sentence="the cat and the hat and the bat"):
    words = sentence.split(" ")
    counts = {word : sentence.count(word) for word in words}
    by_count = {}

    for word, count in counts.items():
        by_count.setdefault(count, []).append(word)

    return {
        "counts" : counts,
        "most_common" : max(counts.keys()),
        "by_count" : by_count,
        "singles": by_count.get(1)
    }


# ---------------------------------------------------------------------------
# Problem 3: Nested dicts
# Given a dict of student -> list of scores, return a dict mapping each student
# to a small report dict with:
#     "scores"  -> the list of scores
#     "average" -> the mean rounded to 1 decimal place
#     "best"    -> the highest score
#     "passed"  -> True if the average is 60 or more
# Also add a "class_average" key at the top level: the mean of every score,
# rounded to 1 decimal place.
# (Test with {"ana": [90, 80], "bob": [50, 55]}
#  -> ana average 85.0 passed True, bob average 52.5 passed False,
#     class_average 68.8)
# ---------------------------------------------------------------------------
def problem_3(grades={"ana": [90, 80], "bob": [50, 55]}):
      avg_dicts = {}

      for k, v in grades.items():
          avg_dicts[k] = float(f"{statistics.mean(grades[k]):.1f}")

      print(avg_dicts)

      pass_dicts = {}
      for k, v in avg_dicts.items():
          pass_dicts[k] = v > 60

      ret_str = ""

      for k, v in avg_dicts.items():
          ret_str += f"{k} average {v} passed {pass_dicts[k]} "


      print(avg_dicts.values())

      class_avg = sum(avg_dicts.values()) / len(avg_dicts)

      ret_str += f"class_average {class_avg:.1f}"

      return ret_str


if __name__ == "__main__":
    print("Problem 1 (safe reads/writes):", problem_1())
    print("Problem 2 (counting):", problem_2())
    print("Problem 3 (nested dicts):", problem_3())
