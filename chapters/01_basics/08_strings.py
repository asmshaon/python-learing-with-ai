"""
Chapter 08: Python Strings
==========================

Notes
-----
- Strings are IMMUTABLE sequences of characters. s[0] = "x" raises TypeError;
  every "modification" method returns a NEW string.
- Indexing and slicing:
      s = "python"
      s[0]      -> 'p'        first character
      s[-1]     -> 'n'        negative indexes count from the end
      s[1:4]    -> 'yth'      slice: start included, END EXCLUDED
      s[:3]     -> 'pyt'      omitted start = beginning
      s[3:]     -> 'hon'      omitted end = through the last char
      s[::2]    -> 'pto'      third number is the step
      s[::-1]   -> 'nohtyp'   step -1 reverses the string
- len(s) gives the length; "th" in s membership-tests a substring.
- The methods you will use constantly (all return NEW strings):
      s.upper()  s.lower()  s.title()  s.capitalize()
      s.strip()              trim whitespace both ends (.lstrip/.rstrip)
      s.replace(old, new)    replace ALL occurrences
      s.split(sep)           -> list of parts; sep=None splits on any spaces
      sep.join(list)         inverse of split: "-".join(["a","b"]) -> "a-b"
      s.startswith(x)  s.endswith(x)  s.find(x)   (find returns -1, not error)
      s.count(x)             how many non-overlapping occurrences
- f-strings are the modern way to build strings:
      name = "Ada"; f"Hello {name}, {2 + 3}"  -> 'Hello Ada, 5'
  (format specs like f"{pi:.2f}" are covered in the String Formatting chapter.)
- Strings compare alphabetically by Unicode code point: "apple" < "banana" is
  True, but "Zoo" < "apple" is also True because uppercase sorts first.

Run:  python3 chapters/01_basics/08_strings.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Slicing drills
# Given a string, return a tuple of five slices, in this order:
#     first 3 characters
#     last 3 characters
#     every second character (step 2, from the start)
#     the string reversed
#     the middle character (index len // 2)
# (Test with "programming"
#  -> expected ('pro', 'ing', 'pormig', 'gnimmargorp', 'a'))
# ---------------------------------------------------------------------------
from operator import le
import re


def problem_1(s="programming"):
    return (s[:3], s[-3:], s[::2], s[::-1], s[len(s) // 2])


# ---------------------------------------------------------------------------
# Problem 2: Clean and analyze a sentence
# Given a messy sentence, return a dict with these keys:
#     "clean"  the sentence stripped of outer whitespace and lowercased
#     "words"  the clean sentence split into a list of words
#     "count"  how many words
#     "longest"  the longest word  -> max(words, key=len)
#     "joined"   the words joined back together with "-"
# (Test with "  The quick brown Fox  "
#  -> expected {'clean': 'the quick brown fox',
#               'words': ['the', 'quick', 'brown', 'fox'],
#               'count': 4, 'longest': 'quick',
#               'joined': 'the-quick-brown-fox'})
# ---------------------------------------------------------------------------
def problem_2(sentence="  The quick brown Fox  "):
    setResult = {}

    setResult["clean"] = sentence
    setResult["words"] = sentence.strip().split(" ")
    setResult["count"] = len(setResult["words"])
    setResult["longest"] = max(setResult["words"], key=len)
    setResult["joined"] = "-".join(setResult["words"])

    return setResult


# ---------------------------------------------------------------------------
# Problem 3: Palindrome check (ignoring case and spaces)
# A palindrome reads the same forwards and backwards. Normalize the string
# first — lowercase it and remove spaces (hint: s.replace(" ", "")) — then
# compare it with its reverse (s[::-1]). Return True or False.
# (Test defaults: "Never odd or even" -> True, and try "python" -> False)
# ---------------------------------------------------------------------------
def problem_3(s="Never odd or even"):
    return s[::-1] == s.lower().replace(" ", "")


if __name__ == "__main__":
    print("Problem 1 (slicing):", problem_1())
    print("Problem 2 (clean/analyze):", problem_2())
    print("Problem 3 (palindrome):", problem_3())
