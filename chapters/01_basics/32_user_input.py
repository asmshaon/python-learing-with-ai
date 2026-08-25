"""
Chapter 32: Python User Input
=============================

Notes
-----
- input(prompt) reads ONE LINE of text from the user and ALWAYS returns a
  string. It prints the prompt, waits for Enter, and blocks the program until
  then:
      name = input("Your name: ")
  Note: no newline after the prompt, and the returned string has its trailing
  newline stripped.
- A value typed as digits is still TEXT. "42" is not the number 42, so convert
  before using:
      age = int(input("Age: "))       # float(...) for decimals
  A bad conversion raises ValueError and CRASHES the program — wrap it in
  try/except when you cannot trust the user:
      try:
          age = int(input("Age: "))
      except ValueError:
          age = None   # or re-ask
- input() returns the text VERBATIM. Strip surrounding whitespace first, or a
  stray space breaks the conversion:
      name = input("Name: ").strip()
  A completely empty line comes back as "" — that is a valid input to check
  for (empty strings are falsy).
- In a script run with piped/redirected stdin, input() reads from the pipe
  instead of the keyboard. When the pipe runs out of lines, input() raises
  EOFError — catch it if your script may be fed a short pipe.
- KeyboardInterrupt (Ctrl-C) can arrive while input() is waiting — also
  catchable with try/except.
- Because the loop runs interactively, the problems here take the "typed" text
  as a plain string ARGUMENT instead of calling input() directly, so they are
  runnable and testable. In real use you would pass input("...") in.
- Tiny helpers worth knowing:
      input().strip()          strip the line
      input().split()          split on whitespace -> list of words
      input().lower()          case-blind comparisons
- Prompt wording is a choice, not syntax. Keep prompts short and end with a
  space so the user's answer starts right after the prompt.

Run:  python3 chapters/01_basics/32_user_input.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Read text and turn it into numbers safely
# Write a helper read_int(prompt) that behaves like input() PLUS conversion:
#   it prints prompt, reads a line, strips it, and returns int() of the line.
#   It must NOT crash — on a ValueError it returns None instead. (So the tests
#   can call it, this chapter's functions take the line as an argument: write
#   read_int(prompt, line) where "line" is the text the user would have typed.)
# Part A — read_int("age: ", " 42 ") must return 42 (note the spaces).
# Part B — read_int("age: ", "abc") must return None, not raise.
# Part C — read_int("age: ", "") (empty line) must also return None.
# Part D — a helper read_float(prompt, line) doing the same with float, and
#   read_bool(prompt, line) that returns True for "y"/"yes"/"1" and False for
#   "n"/"no"/"0", everything case-insensitive, and None for anything else.
# Part E — a helper ask_until_int(prompt, lines) that is handed a LIST of typed
#   lines (one per attempt) and returns the FIRST one that converts — on the
#   given ["bad", "12"] it must return 12. If none convert, return None.
# Return a dict with keys:
#   "clean"        -> read_int("age: ", " 42 ")
#   "bad"          -> read_int("age: ", "abc")
#   "empty"        -> read_int("age: ", "")
#   "float_ok"     -> read_float("price: ", " 9.99")
#   "bool_yes"     -> read_bool("again? ", "YES")
#   "bool_no"      -> read_bool("again? ", "no")
#   "bool_mixed"   -> read_bool("again? ", "maybe")
#   "retried"      -> ask_until_int("age: ", ["bad", "12"])
#   "never_ok"     -> ask_until_int("age: ", ["bad", "worse"])
# (Expected: {'clean': 42, 'bad': None, 'empty': None, 'float_ok': 9.99,
#             'bool_yes': True, 'bool_no': False, 'bool_mixed': None,
#             'retried': 12, 'never_ok': None})
# ---------------------------------------------------------------------------
def read_int(prompt, line):
    try:
        return int(line.strip())
    except ValueError:
        return None


def read_float(prompt, line):
    try:
        return float(line.strip())
    except ValueError:
        return None


def read_bool(prompt, line):
    line = line.strip().lower()

    try:
        if line in ["y", "yes", "1"]:
            return True
        if line in ["n", "no", "0"]:
            return False
    except:
        return None


def ask_until_int(prompt, lines):
    try:
        for line in lines:
            try:
                return int(line.strip())
            except:
                continue
    except:
        return None


def problem_1():
    return {
        "clean": read_int("age: ", " 42 "),
        "bad": read_int("age: ", "abc"),
        "empty": read_int("age: ", ""),
        "float_ok": read_float("price: ", " 9.99"),
        "bool_yes": read_bool("again? ", "YES"),
        "bool_no": read_bool("again? ", "no"),
        "bool_mixed": read_bool("again? ", "maybe"),
        "retried": ask_until_int("age: ", ["bad", "12"]),
        "never_ok": ask_until_int("age: ", ["bad", "worse"]),
    }


# ---------------------------------------------------------------------------
# Problem 2: One line, several fields, and a validation gate
# The user answers a survey by typing several values on ONE line, separated by
# commas, e.g. "Ada,36,Dhaka" or "Linus,29". Some fields are optional.
# Part A — write split_fields(line) that splits on "," and strips each piece.
#   Handle a missing field: if there are fewer than 3 pieces, pad the result
#   with "" up to length 3; if there are more than 3, keep the first 3.
# Part B — write build_profile(line) that turns the line into a dict
#   {"name": ..., "age": int, "city": ...}. The age must be an int if the text
#   converts, otherwise None (never crash). The name and city are the stripped
#   strings. An empty line ("") must come out as all-"" / None fields.
# Part C — write is_valid(profile) that returns True only when name is
#   non-empty AND age is an int (not None) AND age is at least 18. This is the
#   gate a program would use before saving the profile.
# Part D — write ask_age_year(birth_line) where the user types their birth
#   year ("1995") — return their age in 2026 as an int, or None on bad input.
#   For testability it takes the typed line, not input().
# Return a dict with keys:
#   "fields_ok"   -> split_fields("  Ada , 36 , Dhaka ")
#   "fields_short"-> split_fields("Ada")
#   "fields_long" -> split_fields("Ada,36,Dhaka,extra")
#   "profile"     -> build_profile("Linus,29,Chittagong")
#   "bad_age"     -> build_profile("Grace,old")
#   "empty_profile"-> build_profile("")
#   "valid_yes"   -> is_valid(build_profile("Ada,36,Dhaka"))
#   "valid_no"    -> is_valid(build_profile("Kid,15,Dhaka"))
#   "age_year"    -> ask_age_year("1995")
#   "age_bad"     -> ask_age_year("not a year")
# (Expected: {'fields_ok': ['Ada', '36', 'Dhaka'], 'fields_short': ['Ada', '', ''],
#             'fields_long': ['Ada', '36', 'Dhaka'],
#             'profile': {'name': 'Linus', 'age': 29, 'city': 'Chittagong'},
#             'bad_age': {'name': 'Grace', 'age': None, 'city': ''},
#             'empty_profile': {'name': '', 'age': None, 'city': ''},
#             'valid_yes': True, 'valid_no': False, 'age_year': 31,
#             'age_bad': None})
# ---------------------------------------------------------------------------
def split_fields(line):
    splits = [l.strip() for l in line.split(",")]

    if len(splits) >= 3:
        return splits[:3]

    if len(splits) < 3:
        n = 3 - len(splits)
        splits += [""] * n
        return splits


def build_profile(line):
    if line == "":
        return {
            "name": "",
            "age": None,
            "city": "",
        }

    splits = line.split(",")

    name = splits[0] if len(splits) >= 1 else ""
    city = splits[2] if len(splits) >= 3 else ""

    try:
        age = int(splits[1]) if len(splits) >= 2 else None
    except:
        age = None

    return {
        "name": name.strip(),
        "age": age,
        "city": city.strip(),
    }


def is_valid(profile):
    if (
        profile.get("name") != ""
        and profile.get("age") is not None
        and profile.get("age") >= 18
    ):
        return True

    return False


def ask_age_year(birth_line):
    try:
        birth_year = int(birth_line)
        return 2026 - birth_year
    except ValueError:
        return None


def problem_2():
    return {
        "fields_ok": split_fields("  Ada , 36 , Dhaka "),
        "fields_short": split_fields("Ada"),
        "fields_long": split_fields("Ada,36,Dhaka,extra"),
        "profile": build_profile("Linus,29,Dhaka"),
        "bad_age": build_profile("Grace,old"),
        "empty_profile": build_profile(""),
        "valid_yes": is_valid(build_profile("Ada,36,Dhaka")),
        "valid_no": is_valid(build_profile("Kid,15,Dhaka")),
        "age_year": ask_age_year("1995"),
        "age_bad": ask_age_year("not a year"),
    }


# ---------------------------------------------------------------------------
# Problem 3: A tiny menu loop and a login gate
# Build the LOGIC of a command-line menu. In a real program the loop would be:
#       while True:
#           choice = input("> ").strip().lower()
#           if choice == "quit": break
#           ...
#   The problems below take the list of typed lines instead, so they are
#   testable. Model the loop with a for over the lines and a break.
# Part A — write menu(lines) that walks each typed line, lowercases and strips
#   it, and:
#       "start" -> appends "starting" to a log
#       "stop"  -> appends "stopping" to the log
#       "quit"  -> appends "bye" and BREAKS (nothing after is processed)
#       anything else -> appends "unknown: <line>"
#   Return the log list. On ["start", "stop", "quit", "start"] it must give
#   ["starting", "stopping", "bye"] — the trailing "start" never runs.
# Part B — write gate(lines, users) where users is {"ada": "1234"}: each line
#   is "user password". A line is ACCEPTED when the user exists AND the
#   password matches; otherwise it is REJECTED. Stop at the first accepted
#   login. Return the dict {"accepted": user, "attempts": n} — attempts counts
#   every line processed before and including the accepted one. If nothing is
#   accepted, accepted is None.
# Part C — write prompt_line(prompt) that is a stand-in for input(prompt): it
#   records the prompt it was given (so we can verify the prompt is used) and
#   returns the next line from a queue of canned answers. Demonstrate it by
#   reading two prompts with the canned answers ["Ada", "36"] and returning the
#   tuple (prompts_used, values_read).
# Return a dict with keys:
#   "menu_log"     -> menu(["start", "stop", "quit", "start"])
#   "menu_unknown" -> menu(["jump"])
#   "login_ok"     -> gate(["bob x", "ada 1234"], users)
#   "login_fail"   -> gate(["ada 0000", "bob x"], users)  (nothing accepted)
#   "login_reject" -> gate(["ada 0000", "ada 1234"], users) (1st rejected, 2nd ok)
#   "prompt_pair"  -> the (prompts, values) tuple from Part C
# (Expected: {'menu_log': ['starting', 'stopping', 'bye'],
#             'menu_unknown': ['unknown: jump'],
#             'login_ok': {'accepted': 'ada', 'attempts': 2},
#             'login_fail': {'accepted': None, 'attempts': 2},
#             'login_reject': {'accepted': 'ada', 'attempts': 2},
#             'prompt_pair': (['user: ', 'age: '], ['Ada', '36'])})
# ---------------------------------------------------------------------------


def menu(lines):
    log = []

    for line in lines:
        sl = line.strip().lower()

        match (sl):
            case "start":
                log.append("starting")

            case "stop":
                log.append("stopping")

            case "quit":
                log.append("bye")
                break

            case _:
                log.append("unknown: " + sl)

    return log


def gate(lines, users):
    attempts = 0
    accepted = None

    for line in lines:
        attempts += 1

        splits = line.split()

        if len(splits) >= 2:
            name = splits[0]
            password = splits[1]

            if name in users and users[name] == password:
                accepted = name
                break

    return {
        "accepted": accepted,
        "attempts": attempts,
    }


def prompt_line(prompt, answers, prompts_used):
    prompts_used.append(prompt)
    return answers.pop(0)


def problem_3():
    users = {"ada": "1234"}
    answers = ["Ada", "20"]
    prompts_used = []

    values = [
        prompt_line("user: ", answers, prompts_used),
        prompt_line("age: ", answers, prompts_used),
    ]

    return {
        "menu_log": menu(["start", "stop", "quit", "start"]),
        "menu_unknown": menu(["jump"]),
        "login_ok": gate(["bob x", "ada 1234"], users),
        "login_fail": gate(["ada 0000", "bob x"], users),
        "login_reject": gate(["ada 0000", "ada 1234"], users),
        "prompt_pair": (prompts_used, values),
    }


if __name__ == "__main__":
    print("Problem 1 (safe input):", problem_1())
    print("Problem 2 (fields + gate):", problem_2())
    print("Problem 3 (menu + login):", problem_3())
