"""
Chapter 18: Python For Loops
============================

Notes
-----
- A for loop walks over the items of any ITERABLE — list, tuple, set, dict,
  string, range, file:
      for color in ["red", "green"]:
          print(color)
  You get the ITEMS, not the indexes.
- Over a string you get characters; over a dict you get KEYS. For pairs use
  .items():
      for key, value in person.items(): ...
- range(stop) / range(start, stop) / range(start, stop, step) generates numbers
  when you really do need counting. range(5) -> 0,1,2,3,4 (stop excluded).
- enumerate gives index AND item — better than range(len(...)):
      for i, item in enumerate(items, start=1): ...
- zip walks several iterables side by side and stops at the SHORTEST:
      for name, score in zip(names, scores): ...
- break / continue / else work exactly as in while: else runs only if the loop
  finished WITHOUT a break.
- Nested loops: the inner loop runs fully for every step of the outer one.
  break only leaves the loop it is in.
- Do not add or remove items from the list you are looping over — loop over a
  copy (items[:]) or build a new list instead.
- Comprehensions are for loops that BUILD something:
      [n * 2 for n in nums if n > 0]        list
      {k: v for k, v in pairs}              dict
      {c for c in text}                     set
  Use a plain for loop when the body does more than produce one value.
- sorted(), reversed(), sum(), min(), max(), any(), all() often replace a whole
  hand-written loop — reach for them first.

Run:  python3 chapters/01_basics/18_for_loops.py
"""


# ---------------------------------------------------------------------------
# Problem 1: enumerate and zip
# Given a list of names and a list of scores, return a list of strings, one per
# pair, numbered from 1:
#     "1. ana - 90"
# If the lists are different lengths, the extra items are simply ignored.
# (Test with ["ana", "bob", "cid"] and [90, 75]
#  -> expected ['1. ana - 90', '2. bob - 75'])
# ---------------------------------------------------------------------------
def problem_1(names=("ana", "bob", "cid"), scores=(90, 75)):
    result = []

    for index, (name, score) in enumerate(zip(names, scores), start=1):
        result.append(f"{index}. {name} - {score}")

    return result


# ---------------------------------------------------------------------------
# Problem 2: Nested loops
# Build a multiplication table for 1..n as a list of rows, each row a list of
# numbers, using nested for loops. Also return, as a second item, the flat list
# of the diagonal values (1*1, 2*2, ...).
# (Test with 3 -> ([[1, 2, 3], [2, 4, 6], [3, 6, 9]], [1, 4, 9]))
# ---------------------------------------------------------------------------
def problem_2(n=3):
    table = [[0 for _ in range(n)] for _ in range(n)]
    diagonal = []

    for i in range(n):
        for j in range(n):
            table[i][j] = (i + 1) * (j + 1)

            if i == j:
                diagonal.append(table[i][j])

    return table, diagonal


# ---------------------------------------------------------------------------
# Problem 3: Search with for...else
# Given a list of numbers and a target, loop over the list and:
#   - return {"found": True, "index": i} for the FIRST item equal to target
#   - if the loop finishes without finding it, use the for loop's else clause
#     to return {"found": False, "index": -1}
# Then do the same thing a second way and include it in the result: a
# comprehension building "seen_before" -> the list of items you looked at before
# the match (empty list when not found).
# Return a dict with keys "found", "index", "seen_before".
# (Test with [4, 8, 15, 16] and target 15
#  -> expected {'found': True, 'index': 2, 'seen_before': [4, 8]})
# ---------------------------------------------------------------------------
def problem_3(numbers=(4, 8, 15, 16), target=15):
    found = False
    index = 0
    seen_before = []

    for n in numbers:
        if n == target:
            found = True
            break

        seen_before.append(numbers[index])
        index += 1
    else:
        index = -1

    return {
        "found" : found,
        "index" : index,
        "seen_before" : seen_before
    }


if __name__ == "__main__":
    print("Problem 1 (enumerate/zip):", problem_1())
    print("Problem 2 (nested loops):", problem_2())
    print("Problem 3 (for...else search):", problem_3())
