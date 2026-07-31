"""
Chapter 11: Python Lists
========================

Notes
-----
- A list is an ORDERED, MUTABLE, indexable collection that allows duplicates:
      nums = [3, 1, 4, 1, 5]
- Indexing / slicing works exactly like strings (start included, end excluded):
      nums[0]  nums[-1]  nums[1:3]  nums[::-1]
  but unlike strings, lists are mutable: nums[0] = 99 works.
- Adding items:
      lst.append(x)          add one item to the end
      lst.insert(i, x)       insert x at index i
      lst.extend(other)      add every item from another iterable
      a + b                  concatenate into a NEW list
- Removing items:
      lst.remove(x)          remove first matching VALUE (ValueError if absent)
      lst.pop(i)             remove & RETURN item at index i (default last)
      del lst[i]             delete by index
      lst.clear()            empty the list
- Ordering:
      lst.sort()             sort IN PLACE (add reverse=True or key=...)
      sorted(lst)            return a NEW sorted list, original untouched
      lst.reverse()          reverse in place
- Useful helpers:  len, sum, min, max, lst.index(x), lst.count(x), x in lst.
- List comprehensions build lists concisely:
      [n * n for n in range(5)]            -> [0, 1, 4, 9, 16]
      [n for n in nums if n % 2 == 0]      -> keep only evens
- Careful: assignment does NOT copy. b = a makes both names point at the SAME
  list. To copy use a.copy(), list(a), or a[:].

Run:  python3 chapters/01_basics/11_lists.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Build and mutate a list
# Start from a copy of the given list, then:
#   - append 99
#   - insert 0 at the front
#   - remove the value 4 (if present)
# Return the resulting list. Do NOT mutate the caller's original list.
# (Test with [3, 1, 4, 1, 5]
#  -> expected [0, 3, 1, 1, 5, 99])
# ---------------------------------------------------------------------------
import re


def problem_1(nums=(3, 1, 4, 1, 5)):
    cp_list = list(nums)

    cp_list.append(99)
    cp_list.insert(0, 0)
    cp_list.remove(4)

    return cp_list


# ---------------------------------------------------------------------------
# Problem 2: Summary statistics
# Given a list of numbers, return a dict describing it:
#     "length", "total" (sum), "smallest", "largest",
#     "sorted_desc" (a NEW list sorted high -> low),
#     "unique" (sorted list of the distinct values)
# (Test with [5, 2, 5, 8, 1]
#  -> expected {'length': 5, 'total': 21, 'smallest': 1, 'largest': 8,
#               'sorted_desc': [8, 5, 5, 2, 1], 'unique': [1, 2, 5, 8]})
# ---------------------------------------------------------------------------
def problem_2(numbers=(5, 2, 5, 8, 1)):
    numbers = list(numbers)

    return {
        "length": len(numbers),
        "total": sum(numbers),
        "smallest": min(numbers),
        "largest": max(numbers),
        "sorted_desc": sorted(numbers, reverse=True),
        "unique": set(numbers),
    }


# ---------------------------------------------------------------------------
# Problem 3: Comprehension drills
# Given a list of integers, return a tuple of three NEW lists:
#     squares of every number
#     only the even numbers
#     each number labelled "even"/"odd" as strings
# (Test with [1, 2, 3, 4]
#  -> expected ([1, 4, 9, 16], [2, 4], ['odd', 'even', 'odd', 'even']))
# ---------------------------------------------------------------------------
def problem_3(numbers=(1, 2, 3, 4)):
    squares = [n**2 for n in numbers]
    evens = [n for n in numbers if n % 2 == 0]
    labels = ["even" if n % 2 != 0 else "odd" for n in numbers]

    return (squares, evens, labels)


if __name__ == "__main__":
    print("Problem 1 (build/mutate):", problem_1())
    print("Problem 2 (summary stats):", problem_2())
    print("Problem 3 (comprehensions):", problem_3())
