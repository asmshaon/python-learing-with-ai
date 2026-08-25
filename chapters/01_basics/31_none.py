"""
Chapter 31: Python None
=======================

Notes
-----
- None is Python's single "nothing here" value. It is the ONLY member of the
  NoneType type:  type(None).__name__  ->  "NoneType".
- It is a SINGLETON — there is exactly one None in a whole program. That is why
  you compare with the IDENTITY operator, never with ==:
      x is None     x is not None
  The built-in == can be fooled by an object whose __eq__ is written to claim
  equality with anything (None == None is fine, but a custom object could make
  None == obj True; `is` cannot be lied to).
- None is FALSY:  bool(None) is False. So `if x:` skips when x is None, and
  `if x is not None:` is the explicit way to say "x has a value".
- A LOT of things quietly return None:
      a function with no return statement
      a function that hits return with no value
      print(...)   list.sort()   dict.update()   .append()/.extend()/.insert()
      d.get(key) when the key is missing (unless you pass a default)
      re.search(...) when the pattern does not match
  So None is both the "no result" of missing data AND the "void" return of
  mutating methods. This is why x = d.get(k) then x.sort() crashes with
  AttributeError: 'NoneType' object has no attribute 'sort'.
- None as a DEFAULT ARGUMENT is the standard fix for the mutable-default trap.
  A default is created ONCE at def time, so def f(items=[]) shares one list
  across every call. Use the sentinel pattern instead:
      def f(items=None):
          if items is None:
              items = []
  Now every call gets its own fresh list.
- Functions that FAIL should signal it honestly: either raise an exception or
  return None (and the caller checks `is not None`). Returning None silently
  hides bugs; raising delays the crash. Pick per situation.
- Common pattern — safe lookup that returns None on a miss:
      mapping.get(key)          missing key -> None
      dict.get(key, default)    missing key -> default
- None is not the empty string "" or 0 or False. They are all falsy, but only
  None means "no value at all". An empty list [] and None are different too:
  JSON null, CSV blank cells, and SQL NULL all map onto None.

Run:  python3 chapters/01_basics/31_none.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Recognise None everywhere
# Part A — the basics: what type is None (type name), does None == None, and
#   does a bare `if None:` run (is None falsy)?
# Part B — capture the return values of functions and methods that silently
#   return None: a function with no return, print("hi"), [1, 2].append(3),
#   {}.update({"a": 1}), and [3, 1, 2].sort(). Record whether each returned
#   None. WATCH OUT: calling .append/.sort in a dict value would crash later —
#   just test the return value here.
# Part C — show that `is` and `==` can disagree: build a tiny class whose
#   __eq__ always returns True, then compare None == obj (True!) against
#   None is obj (False).
# Part D — dict.get: with d = {"a": 1}, get the key "a", the missing key "z",
#   and the missing key "z" with a default of 0.
# Part E — a None-valued key: d2 = {"a": None}; is d2.get("a") None? How would
#   you tell "key present but None" from "key absent" (hint: the `in` operator
#   on the dict, or .keys())?
# Return a dict with keys:
#   "type_name"       -> the type name of None
#   "none_eq_none"    -> True/False for None == None
#   "none_is_none"    -> True/False for None is None
#   "none_falsy"      -> True if bool(None) is False
#   "silent_returns"  -> list of the five return values from Part B
#   "eq_lies"         -> bool(None == obj) from Part C
#   "is_truthful"     -> bool(None is obj) from Part C
#   "found"           -> d.get("a")
#   "missing"         -> d.get("z")
#   "with_default"    -> d.get("z", 0)
#   "none_value"      -> d2.get("a") (the key IS present, value is None)
#   "key_present"     -> True/False: is "a" in d2
# (Expected: {'type_name': 'NoneType', 'none_eq_none': True,
#             'none_is_none': True, 'none_falsy': True,
#             'silent_returns': [None, None, None, None, None],
#             'eq_lies': True, 'is_truthful': False, 'found': 1,
#             'missing': None, 'with_default': 0, 'none_value': None,
#             'key_present': True})
# ---------------------------------------------------------------------------


# Part B — capture the return values of functions and methods that silently
#   return None: a function with no return, print("hi"), [1, 2].append(3),
#   {}.update({"a": 1}), and [3, 1, 2].sort(). Record whether each returned
#   None. WATCH OUT: calling .append/.sort in a dict value would crash later —
#   just test the return value here.
def with_no_return():
    pass


class TinyClass:
    def __eq__(self, other):
        return True


def problem_1():
    obj = TinyClass()
    d = {"a": 1}
    d2 = {"a": None}

    return {
        "type_name": type(None).__name__,
        "none_eq_none": None == None,
        "none_is_none": None is None,
        "none_falsy": bool(None) is False,
        "silent_returns": [
            with_no_return(),
            print("hi"),
            [1, 2].append(3),
            {}.update({"a": 1}),
            [3, 1, 2].sort(),
        ],
        "eq_lies": None == obj,
        "is_truthful": None is obj,
        "found": dict.get(d, "a"),
        "missing": dict.get(d, "b"),
        "with_default": dict.get(d, "z", 0),
        "none_value": d2.get("a"),
        "key_present": "a" in d2.keys(),
    }


# ---------------------------------------------------------------------------
# Problem 2: None as a sentinel for optional arguments
# Part A — write add_item(items, name) that APPENDS name to items and returns
#   the list. Give items a default of None and create a fresh [] inside when it
#   is None (the sentinel pattern). Call it three times WITHOUT passing items:
#   each call must return its OWN list — prove independence by adding "a" to
#   the first result and "b" to the second and checking the first one has no
#   "b".
# Part B — write count_none(values) that returns how many of the values are
#   None, counted with `is` (never ==).
# Part C — write clean_rows(rows) that drops every sub-list that contains any
#   None in it and returns the survivors.
# Part D — write first_or_none(values) that returns the first value that is not
#   None, or None if there is none. On ["", None, 0, "ok"] it must return "ok"
#   — note "" and 0 are falsy but NOT None, so they count as values.
# Return a dict with keys:
#   "first"      -> the result of the first add_item() call
#   "second"     -> the result of the second add_item() call
#   "independent"-> True if the first call's list has no "b"
#   "none_count" -> count_none([None, 1, None, None, 2])
#   "survivors"  -> clean_rows([[1, 2], [3, None], [None], [4, 5], []])
#   "first_ok"   -> first_or_none(["", None, 0, "ok"])
#   "no_match"   -> first_or_none([None, None])
# (Expected: {'first': ['a'], 'second': ['b'], 'independent': True,
#             'none_count': 3, 'survivors': [[1, 2], [4, 5], []],
#             'first_ok': 'ok', 'no_match': None})
# ---------------------------------------------------------------------------
def add_item(items=None, item=None):
    if items is None:
        items = []

    items.append(item)

    return items


def count_none(values):
    count = 0

    for v in values:
        if v is None:
            count += 1

    return count


def first_or_none(values):
    for v in values:
        if v is not None and v:
            return v


def clean_rows(rows):
    clean_rows = []

    for r in rows:
        none_found = False

        for c in r:
            if c is None:
                none_found = True
                break

        if not none_found:
            clean_rows.append(r)

    return clean_rows


def problem_2():
    first = add_item([], "a")
    second = add_item([], "b")
    add_item([], "c")

    return {
        "first": first,
        "second": second,
        "independent": "b" not in first,
        "none_count": count_none(["1", None]),
        "survivors": clean_rows([[1, 2], [3, None], [None], [4, 5], []]),
        "first_ok": first_or_none(["", None, 0, "ok"]),
        "no_match": first_or_none([None, None]),
    }


# ---------------------------------------------------------------------------
# Problem 3: None means "missing" — build a safe data pipeline
# You work on a log of sales; each record is a dict that may be MISSING keys,
# and missing means None:
#   records = [
#       {"id": 1, "city": "Dhaka",   "amount": 120.0},
#       {"id": 2, "city": "Chittagong"},
#       {"id": 3, "amount": 45.0},
#       {"id": 4, "city": "Sylhet",  "amount": 0.0},
#       {"id": 5, "city": "Khulna",  "amount": 300.0},
#   ]
# Part A — a row is COMPLETE only if it has BOTH "city" and "amount". Use
#   .get() so a missing key comes back as None, then test `is not None`.
#   Split the records into complete and incomplete lists.
# Part B — among COMPLETE rows only, sum the amounts. 0.0 is a real value —
#   make sure an amount of 0 is counted, not treated as missing.
# Part C — build {id: city} for every row that HAS a city. A row without a
#   city must simply not appear.
# Part D — write safe_get(records, id, key) that returns the value or None.
#   Test it on a key that exists, a key that is missing from a present row,
#   and a record id that does not exist at all.
# Return a dict with keys:
#   "complete"    -> list of complete record dicts
#   "incomplete"  -> list of incomplete record dicts
#   "total"       -> sum of amounts over complete rows
#   "city_by_id"  -> {id: city} for rows that have a city
#   "has"         -> safe_get(records, 1, "amount")
#   "missing"     -> safe_get(records, 2, "amount") (key absent from the row)
#   "no_record"   -> safe_get(records, 99, "amount") (no such id)
# (Expected: {'complete': [{'id': 1, 'city': 'Dhaka', 'amount': 120.0},
#                          {'id': 4, 'city': 'Sylhet', 'amount': 0.0},
#                          {'id': 5, 'city': 'Khulna', 'amount': 300.0}],
#             'incomplete': [{'id': 2, 'city': 'Chittagong'},
#                            {'id': 3, 'amount': 45.0}],
#             'total': 420.0,
#             'city_by_id': {1: 'Dhaka', 2: 'Chittagong', 4: 'Sylhet',
#                            5: 'Khulna'},
#             'has': 120.0, 'missing': None, 'no_record': None})
# ---------------------------------------------------------------------------
def problem_3():
    records = [
        {"id": 1, "city": "Dhaka", "amount": 120.0},
        {"id": 2, "city": "Chittagong"},
        {"id": 3, "amount": 45.0},
        {"id": 4, "city": "Sylhet", "amount": 0.0},
        {"id": 5, "city": "Khulna", "amount": 300.0},
    ]

    complete_list = []
    incomplete_list = []
    total = 0
    city_by_id = {}

    for record in records:
        if (
            record.get("city", None) is not None
            and record.get("amount", None) is not None
        ):
            complete_list.append(record)
            total += record.get("amount", 0)
        else:
            incomplete_list.append(record)

        if record.get("city", None) is not None:
            city_by_id[record.get("id")] = record.get("city")

    return {
        "complete": complete_list,
        "incomplete": incomplete_list,
        "total": total,
        "city_by_id": city_by_id,
        "has": safe_get(records, 1, "amount"),
        "missing": safe_get(records, 2, "amount"),
        "no_record": safe_get(records, 99, "amount"),
    }


def safe_get(records, value, key):
    for record in records:
        if value == record.get("id", None):
            return record.get(key, None)


if __name__ == "__main__":
    print("Problem 1 (recognise None):", problem_1())
    print("Problem 2 (None as sentinel):", problem_2())
    print("Problem 3 (missing data):", problem_3())
