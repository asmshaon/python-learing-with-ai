"""
Chapter 26: Python JSON
=======================

Notes
-----
- JSON is a TEXT format for exchanging data — it is how APIs, config files and
  most of the web move objects around. Python reads and writes it with the
  built-in json module:  import json
- Four functions, and the names follow a rule. The ones ending in "s" work on
  STRINGS; the ones without work on FILES:
      json.loads(text)        JSON text   -> Python object
      json.dumps(obj)         Python obj  -> JSON text
      json.load(file)         read a file -> Python object
      json.dump(obj, file)    Python obj  -> write to a file
  Read "load" as decode (coming IN) and "dump" as encode (going OUT).
- The type mapping is fixed:
      JSON            Python
      object    <->   dict
      array     <->   list
      string    <->   str
      number    <->   int / float
      true      <->   True
      false     <->   False
      null      <->   None
  Note the case: JSON writes true/false/null in lowercase, Python writes
  True/False/None.
- The trip is not perfectly round. A tuple goes OUT as a JSON array and comes
  BACK as a list. Dict keys are always strings in JSON, so {1: "a"} returns as
  {"1": "a"}. Sets, dates and custom objects cannot be encoded at all and raise
  TypeError — pass default=str (or convert them yourself) to handle that.
- Making the output readable:
      json.dumps(obj, indent=2)              pretty, multi-line
      json.dumps(obj, sort_keys=True)        keys in alphabetical order
      json.dumps(obj, separators=(",", ":")) compact, no spaces
      json.dumps(obj, ensure_ascii=False)    keep non-English letters as-is
- Broken JSON raises json.JSONDecodeError (a subclass of ValueError), so wrap
  parsing of anything you did not write yourself in try/except.
- Common gotcha: JSON requires DOUBLE quotes and forbids trailing commas.
  A Python dict printed with print() is NOT valid JSON — use json.dumps().

Run:  python3 chapters/01_basics/26_json.py
"""

from ast import List
from collections import defaultdict
from datetime import date
import json


# ---------------------------------------------------------------------------
# Problem 1: Read JSON text into Python
# You are given this JSON text (note: true / null are lowercase in JSON):
#   raw = '{"name": "Ada", "age": 36, "languages": ["Python", "C"],
#            "active": true, "score": null,
#            "address": {"city": "London", "zip": "E1 6AN"}}'
# Parse it with json.loads and pull the pieces out. Reach into the nested
# "address" object with a second key lookup.
# Return a dict with keys:
#   "type"           -> the type name of the parsed value, e.g. type(x).__name__
#   "name"           -> the name field
#   "age_type"       -> the type name of the age field
#   "first_language" -> the first item of the languages list
#   "city"           -> the city, from inside "address"
#   "active"         -> the active field (a real Python bool)
#   "score_is_none"  -> True if the score field came back as None
#   "keys"           -> the top-level keys, sorted alphabetically
# (Expected: {'type': 'dict', 'name': 'Ada', 'age_type': 'int',
#             'first_language': 'Python', 'city': 'London', 'active': True,
#             'score_is_none': True,
#             'keys': ['active', 'address', 'age', 'languages', 'name',
#                      'score']})
# ---------------------------------------------------------------------------
def problem_1():
    raw = (
        '{"name": "Ada", "age": 36, "languages": ["Python", "C"], '
        '"active": true, "score": null, '
        '"address": {"city": "London", "zip": "E1 6AN"}}'
    )
    data = json.loads(raw)

    return {
        "type": type(data).__name__,
        "name": data["name"],
        "age_type": type(data["age"]).__name__,
        "first_language": data["languages"][0],
        "city": data["address"]["city"],
        "active": data["active"],
        "score_is_none": data["score"] is None,
        "keys": sorted(data.keys()),
    }


# ---------------------------------------------------------------------------
# Problem 2: Write Python out as JSON text
# Work from: book = {"title": "Dune", "year": 1965,
#                    "tags": ["scifi", "classic"], "price": 9.99}
# Part A — produce a COMPACT string with no spaces (separators=(",", ":")),
#   and a version with the keys SORTED alphabetically.
# Part B — pretty-print it with indent=2 and count how many lines that takes.
# Part C — check the round trip: does json.loads(json.dumps(book)) equal book?
# Part D — the lossy edges. Dump {"t": (1, 2)}, load it back, and report the
#   type name that the tuple became. Then try to dump a set and catch the
#   TypeError. Finally dump {"when": date(2024, 3, 15)} using default=str so it
#   succeeds.
# Return a dict with keys:
#   "compact"         -> the compact JSON string
#   "sorted_keys"     -> the sort_keys=True string
#   "pretty_lines"    -> number of lines in the indent=2 version
#   "round_trip"      -> True if loading the dumped text gives back book
#   "tuple_becomes"   -> type name the tuple came back as
#   "set_fails"       -> True if dumping a set raised TypeError
#   "with_default"    -> the date dumped using default=str
# (Expected: {'compact':
#               '{"title":"Dune","year":1965,"tags":["scifi","classic"],'
#               '"price":9.99}',
#             'sorted_keys':
#               '{"price": 9.99, "tags": ["scifi", "classic"], '
#               '"title": "Dune", "year": 1965}',
#             'pretty_lines': 9, 'round_trip': True, 'tuple_becomes': 'list',
#             'set_fails': False, 'with_default': '{"when": "2024-03-15"}'})
# ---------------------------------------------------------------------------
def problem_2():
    book = {"title": "Dune", "year": 1965, "tags": ["scifi", "classic"], "price": 9.99}
    compact = json.dumps(book, separators=(",", ":"))

    set_fails = False
    try:
        json.dumps({"t": (1, 2)})
    except TypeError:
        set_fails = True

    return {
        "compact": compact,
        "sorted_keys": json.dumps(book, sort_keys=True),
        "pretty_lines": len(json.dumps(book, indent=2).splitlines()),
        "round_trip": json.loads(compact) == book,
        "tuple_becomes": type(json.loads(json.dumps((1, 2)))).__name__,
        "set_fails": set_fails,
        "with_default": json.dumps({"when": date(2024, 3, 15)}, default=str),
    }


# ---------------------------------------------------------------------------
# Problem 3: Summarise nested JSON, then save and reload it
# You are given a list of orders, each with a list of items:
#   orders = [
#       {"id": 1, "customer": "Ada",
#        "items": [{"name": "pen", "qty": 3, "price": 1.5},
#                  {"name": "book", "qty": 1, "price": 12.0}]},
#       {"id": 2, "customer": "Linus",
#        "items": [{"name": "mug", "qty": 2, "price": 7.25}]},
#       {"id": 3, "customer": "Ada",
#        "items": [{"name": "lamp", "qty": 1, "price": 20.0}]},
#   ]
# Part A — the total of one order is the sum of qty * price over its items.
#   Build {order id: total}, and the grand total of everything.
# Part B — group the money by customer: {customer name: their total}.
# Part C — write the orders to a JSON file (use tempfile for the path, or a
#   scratch file you delete afterwards) with json.dump, read it back with
#   json.load, and confirm it matches what you started with.
# Part D — dump {1: "a"} and load it back. What happened to the integer key?
#   Report the key you get, as a string.
# Return a dict with keys:
#   "totals"       -> {order id: order total}
#   "grand_total"  -> total of all orders
#   "by_customer"  -> {customer: their total}
#   "file_matches" -> True if the reloaded file equals the original orders
#   "int_key"      -> the key that came back from dumping {1: "a"}
# (Expected: {'totals': {1: 16.5, 2: 14.5, 3: 20.0}, 'grand_total': 51.0,
#             'by_customer': {'Ada': 36.5, 'Linus': 14.5},
#             'file_matches': True, 'int_key': '1'})
# ---------------------------------------------------------------------------
def problem_3():
    orders = [
        {
            "id": 1,
            "customer": "Ada",
            "items": [
                {"name": "pen", "qty": 3, "price": 1.5},
                {"name": "book", "qty": 1, "price": 12.0},
            ],
        },
        {
            "id": 2,
            "customer": "Linus",
            "items": [{"name": "mug", "qty": 2, "price": 7.25}],
        },
        {
            "id": 3,
            "customer": "Ada",
            "items": [{"name": "lamp", "qty": 1, "price": 20.0}],
        },
    ]

    totals = {}
    totals_by_customer = defaultdict(float)

    for order in orders:
        total = sum(item["qty"] * item["price"] for item in order["items"])

        totals[order["id"]] = total
        totals_by_customer[order["customer"]] += total

    with open("data.json", "w") as file:
        json.dump(orders, file)

    with open("data.json", "r") as file:
        data = json.load(file)

    return {
        "totals": totals,
        "grand_total": sum(totals.values()),
        "by_customer": dict(totals_by_customer),
        "file_matches": orders == data,
        "int_key": list(json.loads(json.dumps({1: "a"})).keys())[0],
    }


if __name__ == "__main__":
    print("Problem 1 (JSON text -> Python):", problem_1())
    print("Problem 2 (Python -> JSON text):", problem_2())
    print("Problem 3 (nested data + files):", problem_3())
