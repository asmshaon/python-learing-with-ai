r"""
Chapter 27: Python RegEx
========================

Notes
-----
- A regular expression is a small pattern language for describing text, used to
  FIND, CHECK, SPLIT or REPLACE parts of a string. It lives in the re module:
      import re
- Always write patterns as RAW strings — r"\d+" not "\d+" — otherwise Python
  eats the backslashes before re ever sees them.
- The five functions you will use most:
      re.search(p, s)   first match anywhere        -> Match or None
      re.match(p, s)    must match at the START     -> Match or None
      re.fullmatch(p, s) must match the WHOLE string -> Match or None
      re.findall(p, s)  every match                 -> list of strings
      re.finditer(p, s) every match                 -> Match objects (has spans)
      re.sub(p, new, s) replace matches             -> new string
      re.split(p, s)    split on the pattern        -> list of strings
- A Match object is truthy, and carries: m.group() the matched text,
  m.start(), m.end(), m.span(). A miss returns None, so never call .group()
  before checking the result is not None.
- CHARACTER CLASSES:
      \d digit      \w letter/digit/underscore    \s whitespace
      \D \W \S      the opposites
      .             any character except newline
      [abc]         one of a, b, c        [a-z] a range     [^abc] NOT these
- REPEATS (quantifiers):
      *   0 or more     +   1 or more     ?   0 or 1
      {3} exactly 3     {2,4} 2 to 4      {2,} 2 or more
  They are GREEDY — they take as much as possible. Add ? to make them lazy:
      "<.+>"  on "<b>hi</b>" grabs the whole thing
      "<.+?>" stops at the first > and finds two matches
- ANCHORS:  ^ start of string, $ end of string, \b a word boundary.
- GROUPS: brackets capture part of a match.
      (\d{4})-(\d{2})       m.group(1), m.group(2), m.groups()
      (?P<year>\d{4})       a NAMED group: m.group("year"), m.groupdict()
      (?:...)               a group that does NOT capture
  If the pattern has groups, findall returns the GROUPS, not the whole match —
  one string per match if there is one group, a tuple if there are several.
- In re.sub the replacement can refer back to groups: r"\2 \1" swaps two.
- FLAGS go as the last argument: re.IGNORECASE (case-blind), re.MULTILINE (^
  and $ match on every line), re.DOTALL (. also matches newline).
- Reusing a pattern? Compile it once: p = re.compile(r"\d+") then p.findall(s).

Run:  python3 chapters/01_basics/27_regex.py
"""

import re


# ---------------------------------------------------------------------------
# Problem 1: Find, match, and count
# Work on this text:
#   text = ("Order 1043 shipped on 2024-03-15 to Ada Lovelace, "
#           "order 992 shipped on 2024-04-02 to Alan Turing.")
# Part A — find the FIRST run of digits, and report where it sits.
# Part B — collect every date in the shape 4 digits, dash, 2 digits, dash,
#   2 digits, and report the span of the first one.
# Part C — show the difference between search and match: does the text START
#   with "Order"? Does it START with "shipped"?
# Part D — fullmatch "python" against a pattern of lowercase letters only.
# Part E — count how many times the word "order" appears ignoring case.
# Return a dict with keys:
#   "first_number"    -> the first run of digits, as a string
#   "dates"           -> list of every date found
#   "first_date_span" -> the span() of the first date
#   "starts_order"    -> True if the text starts with "Order"
#   "starts_shipped"  -> True if the text starts with "shipped"
#   "is_all_lower"    -> True if "python" fully matches [a-z]+
#   "order_count"     -> how many "order" matches, case-insensitive
# (Expected: {'first_number': '1043',
#             'dates': ['2024-03-15', '2024-04-02'],
#             'first_date_span': (22, 32), 'starts_order': True,
#             'starts_shipped': False, 'is_all_lower': True,
#             'order_count': 2})
# ---------------------------------------------------------------------------
def problem_1():
    text = "Order 1043 shipped on 2024-03-15 to Ada Lovelace, order 992 shipped on 2024-04-02 to Alan Turing."

    first_number = re.search(r"\d{1,}", text).group()
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
    first_date_span = re.search(r"\d{4}-\d{2}-\d{2}", text).span()
    starts_order = re.search(r"^Order", text) is not None
    starts_shipped = re.search(r"^shipped", text) is not None
    is_all_lower = re.fullmatch("[a-z]+", "python") is not None
    order_count = re.findall(r"(order)", text, flags=re.IGNORECASE)

    return {
        "first_number": first_number,
        "dates": dates,
        "first_date_span": first_date_span,
        "starts_order": starts_order,
        "starts_shipped": starts_shipped,
        "is_all_lower": is_all_lower,
        "order_count": len(order_count),
    }


# ---------------------------------------------------------------------------
# Problem 2: Groups, substitution and splitting
# Work on this three-line log (one string with newlines in it):
#   log = ("2024-03-15 ERROR disk full\n"
#          "2024-03-16 INFO backup done\n"
#          "2024-03-17 WARN low memory")
# Part A — write ONE pattern with three named groups: "date", "level" and
#   "msg" (the message is the rest of the line). Run it over every line with
#   finditer.
# Part B — from those matches, collect the list of levels, the groupdict() of
#   the FIRST line, and the messages of ERROR lines only.
# Part C — with re.sub, replace every date with the text [DATE], then count how
#   many [DATE] markers the result contains.
# Part D — split "a  b\tc\nd" on any run of whitespace.
# Part E — with re.sub and a backreference, swap the two words of "hello world".
# Return a dict with keys:
#   "levels"       -> list of the three levels
#   "first_line"   -> groupdict() of the first match
#   "errors"       -> messages from ERROR lines only
#   "date_markers" -> how many [DATE] the masked log contains
#   "split_ws"     -> the split pieces of "a  b\tc\nd"
#   "swapped"      -> "hello world" with its words swapped
# (Expected: {'levels': ['ERROR', 'INFO', 'WARN'],
#             'first_line': {'date': '2024-03-15', 'level': 'ERROR',
#                            'msg': 'disk full'},
#             'errors': ['disk full'], 'date_markers': 3,
#             'split_ws': ['a', 'b', 'c', 'd'], 'swapped': 'world hello'})
# ---------------------------------------------------------------------------
def problem_2():
    log = (
        "2024-03-15 ERROR disk full\n"
        "2024-03-16 INFO backup done\n"
        "2024-03-17 WARN low memory"
    )

    pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>ERROR|INFO|WARN) (?P<msg>.*)"
    matches = list(re.finditer(pattern, log))

    levels = [m.group("level") for m in matches]
    first_line = matches[0].groupdict()
    errors = [m.group("msg") for m in matches if m.group("level") == "ERROR"]

    masked_log = re.sub(r"\d{4}-\d{2}-\d{2}", "[DATE]", log)
    date_markers = masked_log.count("[DATE]")

    split_ws = re.split(r"\s+", "a  b\tc\nd")

    swapped = re.sub(r"(\w+)\s+(\w+)", r"\2 \1", "hello world")

    return {
        "levels": levels,
        "first_line": first_line,
        "errors": errors,
        "date_markers": date_markers,
        "split_ws": split_ws,
        "swapped": swapped,
    }


# ---------------------------------------------------------------------------
# Problem 3: Validation, and greedy vs lazy
# Part A — compile ONE email pattern and keep only the valid addresses from:
#     ["ada@example.com", "bad@@mail", "linus@kernel.org", "no-at-sign.com"]
#   A valid address here is: letters/digits/dot/plus/dash, then @, then a
#   domain of letters/digits/dash, then a dot, then at least 2 lowercase
#   letters. Anchor it so the WHOLE string has to match.
# Part B — from "call 017-1234-5678 or 018-8765-4321" pull out the full phone
#   numbers, and then the same numbers broken into their three parts using
#   capture groups (findall gives tuples when the pattern has groups).
# Part C — a password is strong if it is at least 8 characters AND contains an
#   uppercase letter, a digit, and a non-alphanumeric character. Test both
#   "Str0ng!pass" and "weakpass".
# Part D — on "<b>hi</b>", show the greedy pattern "<.+>" against the lazy
#   "<.+?>" and report what each finds.
# Return a dict with keys:
#   "valid_emails" -> list of the addresses that passed
#   "phones"       -> list of full phone numbers
#   "phone_parts"  -> list of (prefix, middle, last) tuples
#   "strong"       -> True/False for "Str0ng!pass"
#   "weak"         -> True/False for "weakpass"
#   "greedy"       -> what "<.+>" finds
#   "lazy"         -> what "<.+?>" finds
# (Expected: {'valid_emails': ['ada@example.com', 'linus@kernel.org'],
#             'phones': ['017-1234-5678', '018-8765-4321'],
#             'phone_parts': [('017', '1234', '5678'),
#                             ('018', '8765', '4321')],
#             'strong': True, 'weak': False,
#             'greedy': ['<b>hi</b>'], 'lazy': ['<b>', '</b>']})
# ---------------------------------------------------------------------------
def problem_3():
    emails = [
        "ada@example.com",
        "bad@@mail",
        "linus@kernel.org",
        "no-at-sign.com",
        "invalid@",
    ]
    valid_emails = []

    for email in emails:
        if re.fullmatch(r"[A-Za-z0-9.+-]+@[A-Za-z0-9-]+\.[a-z]{2,}", email) is not None:
            valid_emails.append(email)

    phone_string = "call 017-1234-5678 or 018-8765-4321"
    phones = re.findall(r"\d{3}-\d{4}-\d{4}", phone_string)
    phone_parts = re.findall(r"(\d{3})-(\d{4})-(\d{4})", phone_string)
    pattern = "^(?=.*[0-9])(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{8,}$"

    strong = re.search(f"{pattern}", "Str0ng!pass") is not None
    week = re.search(f"{pattern}", "weakpass") is not None

    html = "<b>hi</b>"

    greedy = re.findall(r"<.+>", html)

    lazy = re.findall(r"<.+?>", html)

    return {
        "valid_emails": valid_emails,
        "phones": phones,
        "phone_parts": phone_parts,
        "strong": strong,
        "weak": week,
        "greedy": greedy,
        "lazy": lazy,
    }


if __name__ == "__main__":
    print("Problem 1 (find + match):", problem_1())
    print("Problem 2 (groups + sub):", problem_2())
    print("Problem 3 (validation):", problem_3())
