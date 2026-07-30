"""
Chapter 19: Python Functions
============================

Notes
-----
- A function is a named, reusable block of code. Define with def, call with ():
      def greet():
          print("hi")
      greet()
  Defining does NOT run the body; calling does.
- PARAMETERS are the names in the definition, ARGUMENTS are the values you pass:
      def greet(name):        # name is a parameter
          ...
      greet("ana")            # "ana" is an argument
- return sends a value back to the caller and ends the function immediately.
  A function with no return (or a bare return) gives back None.
- return can hand back several values at once as a tuple:
      return total, average
      total, average = stats(nums)
- Ways to pass arguments:
      greet("ana")                positional — order matters
      greet(name="ana")           keyword — order does not matter
      def greet(name="friend")    default value, used when the argument is left out
  Positional arguments must come before keyword arguments in a call.
- *args collects extra POSITIONAL arguments into a tuple; **kwargs collects extra
  KEYWORD arguments into a dict:
      def report(title, *scores, **options): ...
  Order in the definition is: normal, *args, defaults, **kwargs.
- DANGER — mutable default arguments. The default is created ONCE, when the
  function is defined, so a default of [] or {} is shared between every call.
  Use None as the default and build the real value inside the body instead.
- SCOPE: names assigned inside a function are LOCAL to that call and disappear
  when it ends. A function can READ an outer name, but assigning to it creates a
  new local one unless you declare global (or nonlocal for an enclosing
  function's name). Prefer parameters and return values over global.
- A docstring is a string as the FIRST statement in the function body; it
  documents what the function does and is readable at runtime via __doc__ or
  help(). Use triple quotes for it.
- Functions are objects: you can store them in variables, put them in lists, and
  pass them to other functions (sorted(..., key=my_function)). A small throwaway
  function can be written inline as a lambda:
      lambda x: x * 2
- A function that calls itself is RECURSIVE. Every recursive function needs a
  BASE CASE that returns without recursing, otherwise it never stops.
- Type hints are optional documentation, not enforced at runtime:
      def add(a: int, b: int) -> int: ...

Run:  python3 chapters/01_basics/19_functions.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Defaults, keyword arguments and *args
# Write a function that builds a receipt line for an order. It takes an item
# name, then any number of prices as extra positional arguments, plus optional
# keyword settings: currency (default "$") and discount as a fraction
# (default 0.0).
# Return a dict with keys:
#   "item"     -> the item name
#   "count"    -> how many prices were passed
#   "subtotal" -> the sum of the prices
#   "total"    -> the subtotal after the discount is applied, rounded to 2 places
#   "label"    -> a string like "pens x3 = $12.60"  (currency + total)
# If no prices are passed at all, count/subtotal/total must be 0 (not an error).
# (Test with "pens", 5.0, 4.0, 5.0, discount=0.1
#  -> expected {'item': 'pens', 'count': 3, 'subtotal': 14.0, 'total': 12.6,
#               'label': 'pens x3 = $12.60'})
# ---------------------------------------------------------------------------
from csv import Error
import re
from statistics import mean


def problem_1(item="pens", *prices, currency="$", discount=0.0):
    subtotal = sum(prices)
    total = round(subtotal - subtotal * discount, 2)

    return {
        "item" : item,
        "count" : len(prices),
        "subtotal" : subtotal,
        "total" : total,
        "label" : f"{item} x{len(prices)} = {currency}{total:.2f}",
    }


# ---------------------------------------------------------------------------
# Problem 2: The mutable default argument trap
# Write a helper that appends a value to a list of logs and returns that list,
# written the BUGGY way — with `logs=[]` as the default. Call it three times
# without passing a list and collect what you get back.
# Then write the same helper the CORRECT way (default None, build a fresh list
# inside) and call it three times the same way.
# Return a dict with keys:
#   "buggy"  -> the list returned by the third buggy call
#   "fixed"  -> the list returned by the third correct call
#   "shared" -> True if the first and second buggy calls returned the SAME list
#               object (check with `is`), else False
# (Expected: {'buggy': ['a', 'b', 'c'], 'fixed': ['c'], 'shared': True})
# ---------------------------------------------------------------------------

def add_log_buggy(value, logs = []):
    logs.append(value)

    return logs

def add_log_fixed(value, logs = None):
    if logs is None:
        logs = []
    
    logs.append(value)

    return logs

def problem_2():
    first_buggy = add_log_buggy("a")
    second_buggy = add_log_buggy("b")
    third_buggy = add_log_buggy("c")

    add_log_fixed("a")
    add_log_fixed("b")
    third_fixed = add_log_fixed("c")

    return {
        "buggy" : third_buggy,
        "fixed" : third_fixed,
        "shared" : first_buggy is second_buggy
    }


# ---------------------------------------------------------------------------
# Problem 3: Multiple return values, recursion and a function as an argument
# Part A — write a function that takes a list of numbers and returns THREE
# values (a tuple): the smallest, the largest, and the average.
# Part B — write a RECURSIVE function that returns the factorial of n, with a
# base case for n == 0 (0! is 1).
# Part C — write a function that takes a list and another FUNCTION, applies that
# function to every item, and returns the new list. Use it with a lambda that
# squares its argument.
# Return a dict with keys "stats", "factorial", "mapped".
# (Test with [3, 1, 4, 1, 5] and n = 5
#  -> expected {'stats': (1, 5, 2.8), 'factorial': 120,
#               'mapped': [9, 1, 16, 1, 25]})
# ---------------------------------------------------------------------------

def stats(list = []):
    return (
        min(list),
        max(list),
        mean(list)
    )

def my_factorial(n=0):
    if n <= 1:
        return 1

    return n * my_factorial(n - 1)



def problem_3(numbers=(3, 1, 4, 1, 5), n=5):
    return {
        "stats" : stats(numbers),
        "factorial" : my_factorial(n),
        "mapped" : [n*n for n in numbers]
    }


if __name__ == "__main__":
    print("Problem 1 (args/kwargs/defaults):", problem_1("pens", 5.0, 4.0, 5.0, discount=0.1))
    print("Problem 2 (mutable default trap):", problem_2())
    print("Problem 3 (returns/recursion/lambda):", problem_3())
