"""
Chapter 17: Python While Loops
==============================

Notes
-----
- A while loop repeats as long as its condition stays True:
      n = 5
      while n > 0:
          print(n)
          n -= 1
- Something inside the body must eventually make the condition False, or the
  loop never ends. The classic bug is forgetting the n -= 1.
- break leaves the loop immediately; continue skips to the next check:
      while True:
          if done:
              break
          if skip_this:
              continue
- while ... else: the else block runs when the loop ended NORMALLY (the
  condition went False) — it is SKIPPED if you left via break. Handy for
  "searched everything and found nothing".
- "while True" with a break inside is the normal way to write a loop whose exit
  condition is only known in the middle (menus, retry loops, reading input).
- Use while when the number of repetitions is not known up front (keep asking
  until valid, keep halving until small enough). Use for when you are walking
  over a known collection or range.
- Guard against runaway loops while learning: cap the iterations with a counter
  and break out if it gets absurd.
- The walrus operator := assigns inside the condition:
      while (line := next_line()) is not None:

Run:  python3 chapters/01_basics/17_while_loops.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Countdown and accumulate
# Using a while loop (no for, no sum), count DOWN from n to 1 and return a
# dict with:
#     "sequence" -> list of the numbers visited, in order
#     "total"    -> their sum
#     "steps"    -> how many times the loop body ran
# If n is 0 or negative, return empty/zero values.
# (Test with 5 -> {'sequence': [5, 4, 3, 2, 1], 'total': 15, 'steps': 5})
# ---------------------------------------------------------------------------
from os import path


def problem_1(n=5):
    sequence_list = []
    total = 0
    steps = 0

    while n > 0:
        sequence_list.append(n)
        total += n
        steps += 1
        n -= 1

    return {"sequence": sequence_list, "total": total, "steps": steps}


# ---------------------------------------------------------------------------
# Problem 2: break, continue and the while...else
# Walk a list of numbers with a while loop and an index, and:
#   - skip every negative number (continue)
#   - stop as soon as you hit 0 (break)
#   - otherwise add the number to a running total
# Return a dict with "total", "checked" (how many items you looked at, the 0
# included) and "stopped_early" (True if you broke out, False if the loop ran
# to the end — set it in the loop's else clause).
# (Test with [4, -1, 6, 0, 99]
#  -> expected {'total': 10, 'checked': 4, 'stopped_early': True})
# ---------------------------------------------------------------------------
def problem_2(numbers=[4, -1, 6, 0, 99]):
    total = 0
    checked = 0
    stoped_early = True

    i = 0
    while len(numbers) > i:
        checked += 1

        if numbers[i] < 0:
            i += 1
            continue

        total += numbers[i]

        if numbers[i] == 0:
            break

        i += 1
    else:
        stoped_early = False

    return {"total": total, "checked": checked, "stopped_early": stoped_early}


# ---------------------------------------------------------------------------
# Problem 3: Collatz steps
# The Collatz rule: if n is even, halve it; if odd, use 3n + 1. Repeat until n
# reaches 1. Using a while loop, return a dict with:
#     "path"    -> list of every value from the start down to 1 (both included)
#     "steps"   -> how many transformations that took
#     "peak"    -> the largest value seen along the way
# Raise a ValueError if n is less than 1, and stop after 1000 steps as a safety
# net (return "steps": -1 in that case).
# (Test with 6 -> path [6, 3, 10, 5, 16, 8, 4, 2, 1], steps 8, peak 16)
# ---------------------------------------------------------------------------
def problem_3(n=6):
    if n < 1:
        raise ValueError("n must be at least 1")

    path = [n]
    steps = 0
    peak = n

    i = 0
    while n > 1:
        if steps >= 1000:
            return {
                "path": path,
                "steps": -1,
                "peak": peak,
            }

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        path.append(n)

        peak = max(peak, n)

        steps += 1

    return {
        "path": path,
        "steps": steps,
        "peak": peak,
    }


# ---------------------------------------------------------------------------
# Problem 1: Hailstone Until Target
#
# Start with a positive integer n.
#
# Repeatedly:
#   - if n is divisible by 5, divide it by 5
#   - otherwise subtract 2
#
# Stop when:
#   - n becomes exactly 1
#   - n becomes less than 1
#   - or after 100 steps (safety limit)
#
# Return a dict:
#     "path"        -> every value visited (including the starting value)
#     "steps"       -> number of transformations
#     "finished"    -> True if n reached exactly 1, otherwise False
#     "lowest"      -> smallest value encountered
#
# Raise ValueError if n < 1.
# ---------------------------------------------------------------------------
def problem_4(n=25):
    if n < 1:
        raise ValueError("n must be at least 1")

    path = [n]
    steps = 0
    lowest = n
    finished = False

    while n >= 1:
        if steps == 100:
            break

        if n % 5 == 0:
            n //= 5
        else:
            n -= 2

        lowest = min(lowest, n)

        path.append(n)

        steps += 1

        if n == 1:
            finished = True
            break

        if n < 1:
            break
    else:
        finished = True

    return {
        "path": path,
        "steps": steps,
        "finished": finished,
        "lowest": lowest,
    }


# ---------------------------------------------------------------------------
# Problem 2: Consecutive Evens
#
# Walk through a list using a while loop.
#
# Count consecutive even numbers.
#
# If you encounter an odd number:
#     - reset the consecutive count to 0
#
# Stop immediately if you find 4 consecutive even numbers.
#
# Return:
#     {
#         "found": True/False,
#         "checked": number of items examined,
#         "max_streak": longest consecutive even streak
#     }
#
# Example:
# [2,4,6,8,3]
#
# ->
# {
#   "found": True,
#   "checked": 4,
#   "max_streak": 4
# }
# ---------------------------------------------------------------------------
def problem_5(numbers=[2, 4, 6, 8, 3]):
    found = False
    checked = 0
    max_streak = 0
    consecutive_count = 0

    i = 0
    while len(numbers) > i:
        checked += 1
        num = numbers[i]

        if num % 2 != 0:
            consecutive_count = 0
        else:
            consecutive_count += 1

        max_streak = max(max_streak, consecutive_count)

        if max_streak == 4:
            found = True
            break

        i += 1

    return {"found": found, "checked": checked, "max_streak": max_streak}


if __name__ == "__main__":
    print("Problem 1 (countdown):", problem_1())
    print("Problem 2 (break/continue):", problem_2())
    print("Problem 3 (collatz):", problem_3())
    print("Problem 4 (Hailstone):", problem_4(8))
    print("Problem 5 (Consecutive):", problem_5())
