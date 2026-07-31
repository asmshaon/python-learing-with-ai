"""
Chapter 16: Python Match
========================

Notes
-----
- match/case (Python 3.10+) compares a value against PATTERNS, top to bottom,
  and runs the first case that matches:
      match command:
          case "start":
              ...
          case "stop":
              ...
          case _:
              ...
  There is no fall-through, so no break is needed.
- The wildcard "_" is the default case. It matches anything and is usually last.
- Combine alternatives with the | (or) pattern:
      case "quit" | "exit" | "q":
- A CAPTURE pattern binds whatever it matched to a name:
      case other:            # matches anything, other = the value
  Careful: a bare name always matches — it is a capture, not a comparison with
  an existing variable. To compare against a constant, use a dotted name
  (Color.RED, status.OK) or fall back to if/elif.
- Guards add an extra condition with if:
      case n if n < 0:
- Sequence patterns destructure lists / tuples:
      case [x, y]:              exactly two items
      case [first, *rest]:      one or more, rest is a list
      case ("move", direction): a 2-tuple whose first item is "move"
  Strings are NOT treated as sequences here.
- Mapping patterns look at dict keys and ignore extra ones:
      case {"type": "circle", "r": radius}:
- Class patterns match by type, optionally with attributes:
      case str():               any string
      case int() | float():     any number
- Use match when you are branching on the SHAPE or value of one thing;
  a long if/elif chain over unrelated conditions is still fine as an if chain.

Run:  python3 chapters/01_basics/16_match.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Simple command dispatch
# Given a command string, return a message using match/case:
#     "start"              -> "starting..."
#     "stop"               -> "stopping..."
#     "quit", "exit", "q"  -> "bye"          (one case, using |)
#     anything else        -> "unknown command: <command>"  (capture the value)
# (Test with "q" -> "bye"; also check "start" and "dance")
# ---------------------------------------------------------------------------
import re


def problem_1(command="start"):
    match command:
        case "start":
            return "starting..."
        case "stop":
            return "stopping..."
        case "quit" | "exit" | "q":
            return "bye"
        case _:
            return f"unknown command: {command}"


# ---------------------------------------------------------------------------
# Problem 2: Matching shapes of data with guards
# Given a point as a tuple, describe it with match/case:
#     ()            -> "origin missing"
#     (0, 0)        -> "origin"
#     (x, 0)        -> "on the x axis at <x>"
#     (0, y)        -> "on the y axis at <y>"
#     (x, y) where both are positive -> "quadrant I"   (use a guard)
#     any other 2-tuple             -> "somewhere at (<x>, <y>)"
#     3 or more items               -> "not 2D"
# (Test with (0, 5) -> "on the y axis at 5"; also check (), (0, 0), (2, 3),
#  (-1, 4) and (1, 2, 3))
# ---------------------------------------------------------------------------
def problem_2(point=(-1, 4)):
    match point:
        case ():
            return "origin missing"
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"on the x axis at {x}"
        case (0, y):
            return f"on the y axis at {y}"
        case (x, y) if x > 0 and y > 0:
            return "quadrant I"
        case (x, y):
            return f"somewhere at ({x}, {y})"
        case (_, _, *rest):
            return "not 2D"


# ---------------------------------------------------------------------------
# Problem 3: Mapping and class patterns
# Given an "event" dict, turn it into a short summary line with match/case:
#     {"type": "click", "x": .., "y": ..}      -> "click at (x, y)"
#     {"type": "key", "key": ..}               -> "key <key>"
#     {"type": "scroll", "amount": n} where n is negative -> "scroll up <n>"
#     {"type": "scroll", "amount": n}          -> "scroll down <n>"
#     a dict with a "type" key but nothing above -> "unhandled: <type>"
#     anything that is not a dict                -> "not an event"
# Extra keys in the dict should be ignored, not break the match.
# (Test with {"type": "click", "x": 3, "y": 9, "button": "left"}
#  -> expected "click at (3, 9)")
# ---------------------------------------------------------------------------
def problem_3(event={"type": "click", "x": 3, "y": 9, "button": "left"}):
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"click at ({x}, {y})"
        case {"type": "key", "key": key}:
            return f"key {key}"
        case {"type": "scroll", "amount": n} if n < 0:
            return f"scroll up {n}"
        case {"type": "scroll", "amount": n}:
            return f"scroll down {n}"
        case {"type": event_type}:
            return f"unhandled: {event_type}"
        case _:
            return "not an event"


if __name__ == "__main__":
    print("Problem 1 (commands):", problem_1())
    print("Problem 2 (points):", problem_2())
    print("Problem 3 (events):", problem_3())
