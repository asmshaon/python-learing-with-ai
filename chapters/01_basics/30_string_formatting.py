"""
Chapter 30: Python String Formatting
====================================

Notes
-----
- Formatting means building a string out of values, with control over how each
  value LOOKS. Python has three ways; f-strings are the modern default.
      f"Hi {name}"              f-string (3.6+) — use this
      "Hi {}".format(name)      str.format() — still everywhere in old code
      "Hi %s" % name            printf style — legacy, but alive in logging
- An f-string is a normal string with an f in front. Anything inside braces is
  an EXPRESSION that gets evaluated: f"{2 ** 10}" is "1024". To print a literal
  brace, double it: f"{{}}" gives "{}".
- Inside the braces the shape is  {value!conversion:format_spec}
      !r  use repr() instead of str() — f"{'hi'!r}" gives 'hi' with quotes
      !s  use str()   !a  use ascii()
      =   the debug form: with x = 5, f"{x=}" gives "x=5" (name AND value)
- The FORMAT SPEC after the colon is the real power, in this order:
      [[fill]align][sign][#][0][width][grouping][.precision][type]
- ALIGNMENT (the fill character goes BEFORE the align character):
      <  left     >  right     ^  centre     =  pad after the sign (numbers)
      f"{'ok':<8}|"   -> "ok      |"
      f"{'ok':>8}|"   -> "      ok|"
      f"{'ok':^8}|"   -> "   ok   |"
      f"{42:*^9}"     -> "***42****"
  Strings default to LEFT, numbers default to RIGHT.
- NUMBERS:
      f"{3.14159:.2f}"   -> "3.14"        fixed decimals
      f"{1234567:,}"     -> "1,234,567"   thousands separator (_ also works)
      f"{0.256:.1%}"     -> "25.6%"       percent, multiplies by 100
      f"{1234.5:>10,.2f}"-> "  1,234.50"  combine them
      f"{42:05d}"        -> "00042"       zero padding
      f"{7:+d}"          -> "+7"          always show the sign
      f"{12345678:.2e}"  -> "1.23e+07"    scientific
- BASES:  f"{255:b}" "11111111", f"{255:o}" "377", f"{255:x}" "ff",
  and # adds the prefix: f"{255:#x}" -> "0xff".
- STRINGS: .precision TRUNCATES — f"{'internationalization':.6}" is "intern".
- DATES have their own mini-language inside the spec — the strftime codes:
      f"{d:%d %B %Y}" -> "15 March 2024"
- str.format() takes the same specs, and picks values by position or by name:
      "{} {}".format(a, b)        in order
      "{1} {0}".format(a, b)      by index (and an index can repeat)
      "{name}".format(name=x)     by keyword
      "{d[city]}".format(d=data)  index into a dict (no quotes around the key)
- The % style: %s any value, %d integer, %f float, %5.2f width and precision,
  %% a literal percent. Several values go in a TUPLE: "%s is %d" % (name, age).
- format(value, spec) is the same machinery as a plain function, handy when the
  spec is computed: format(3.14159, ".2f").

Run:  python3 chapters/01_basics/30_string_formatting.py
"""

from datetime import date


# ---------------------------------------------------------------------------
# Problem 1: f-strings from the ground up
# Part A — with name = "Ada" and age = 36, build the sentence
#   "Ada is 36 years old".
# Part B — format numbers: pi = 3.14159 to two decimals; 1234567 with thousands
#   separators; the ratio 0.256 as a percentage with one decimal.
# Part C — alignment: put "ok" in a field of 8 left, right and centred, each
#   followed by a "|" so you can see the padding. Then centre 42 in a field of
#   9 padded with "*".
# Part D — expressions and conversions: the value of 2 ** 10 inside an
#   f-string, and "hi" formatted with !r.
# Part E — the debug form: with x = 5, produce the "x=5" output using {x=}.
# Return a dict with keys:
#   "sentence" -> "Ada is 36 years old"
#   "pi"       -> pi to 2 decimals
#   "big"      -> 1234567 with separators
#   "percent"  -> 0.256 as a percentage
#   "left" / "right" / "centre" -> the three padded "ok" strings with the |
#   "stars"    -> 42 centred in 9 with * fill
#   "power"    -> 2 ** 10 as a string
#   "repr_hi"  -> "hi" through !r
#   "debug"    -> the {x=} output
# (Expected: {'sentence': 'Ada is 36 years old', 'pi': '3.14',
#             'big': '1,234,567', 'percent': '25.6%', 'left': 'ok      |',
#             'right': '      ok|', 'centre': '   ok   |',
#             'stars': '***42****', 'power': '1024', 'repr_hi': "'hi'",
#             'debug': 'x=5'})
# ---------------------------------------------------------------------------
def problem_1():
    name = "Ada"
    age = 36
    pi = 3.14159
    x = 5

    return {
        "sentence": f"{name} is {age} years old",
        "pi": f"{pi:.2f}",
        "big": f"{1234567:,}",
        "percent": f"{0.256:.1%}",
        "left": f"{"ok":<8}|",
        "right": f"{"ok":>8}|",
        "centre": f"{"ok":^8}|",
        "stars": f"{"42":*^9}|",
        "power": f"{2**10}",
        "repr_hi": f"{'hi'!r}",
        "debug": f"{x=}",
    }


# ---------------------------------------------------------------------------
# Problem 2: str.format() and the % style
# Part A — with .format(), build "Ada scored 95" from the values "Ada" and 95
#   using empty braces.
# Part B — same two values, but swap them with POSITIONAL INDEXES so you get
#   "95 belongs to Ada". Then build "Ada, Ada!" reusing index 0 twice.
# Part C — use KEYWORD fields to build "Ada lives in Dhaka" from
#   name="Ada", city="Dhaka". Then pull the city out of a dict with
#   data = {"city": "Dhaka"} using the {d[city]} form.
# Part D — pass a format spec through .format(): 1234.5 right aligned in a
#   width of 10, with thousands separators and 2 decimals.
# Part E — the % style: "Ada is 36 years old" from a tuple, and 3.14159 as
#   "%05.2f".
# Return a dict with keys:
#   "simple"   -> "Ada scored 95"
#   "swapped"  -> "95 belongs to Ada"
#   "repeated" -> "Ada, Ada!"
#   "keywords" -> "Ada lives in Dhaka"
#   "from_dict"-> the city pulled out with {d[city]}
#   "spec"     -> 1234.5 formatted with ">10,.2f"
#   "percent_style" -> the % version of the sentence
#   "padded"   -> "%05.2f" applied to 3.14159
# (Expected: {'simple': 'Ada scored 95', 'swapped': '95 belongs to Ada',
#             'repeated': 'Ada, Ada!', 'keywords': 'Ada lives in Dhaka',
#             'from_dict': 'Dhaka', 'spec': '  1,234.50',
#             'percent_style': 'Ada is 36 years old', 'padded': '03.14'})
# ---------------------------------------------------------------------------
def problem_2():
    name = "Ada"
    age = 95
    data = {"city": "Dhaka"}

    return {
        "simple": "{} scored {}".format(name, age),
        "swapped": "{1} belongs to {0}".format(name, age),
        "repeated": "{0}, {0}!".format(name),
        "keywords": "{name} lives in {city}".format(name=name, city=data["city"]),
        "from_dict": "{d[city]}".format(d=data),
        "spec": "{:>10,.2f}".format(1234.5),
        "percent_style": "%s is %s years old" % (name, 36),
        "padded": "%05.2f" % (3.14159),
    }


# ---------------------------------------------------------------------------
# Problem 3: Build a report table
# Work on these rows:
#   rows = [("Apple", 3, 1.5), ("Banana", 12, 0.25), ("Cherry", 250, 0.05)]
# Part A — build the table as a list of strings: a header line, then one line
#   per row. Every line uses the SAME layout — the name left aligned in 10, the
#   quantity right aligned in 5, the price right aligned in 8 with 2 decimals.
#   The header carries "Item", "Qty", "Price" in those same three fields.
# Part B — build a TOTAL line in the same layout: the word "TOTAL", the total
#   quantity, and the total value (each row is quantity times price).
# Part C — number bases: 255 as binary, octal, hex, and hex with the 0x prefix.
# Part D — dates: format date(2024, 3, 15) as "15 March 2024" using the
#   strftime codes inside an f-string.
# Part E — truncation and fill: cut "internationalization" down to 6
#   characters, and right align "ab" in a width of 6 filled with "-".
# Return a dict with keys:
#   "table"    -> list of 4 strings (header + 3 rows)
#   "total"    -> the TOTAL line
#   "bases"    -> [binary, octal, hex, hex with prefix] of 255
#   "day"      -> the formatted date
#   "short"    -> "internationalization" truncated to 6
#   "dashes"   -> "ab" right aligned in 6 with - fill
# (Expected: {'table': ['Item        Qty   Price',
#                       'Apple         3    1.50',
#                       'Banana       12    0.25',
#                       'Cherry      250    0.05'],
#             'total': 'TOTAL       265   20.00',
#             'bases': ['11111111', '377', 'ff', '0xff'],
#             'day': '15 March 2024', 'short': 'intern',
#             'dashes': '----ab'})
# ---------------------------------------------------------------------------
def problem_3():
    rows = [("Apple", 3, 1.5), ("Banana", 12, 0.25), ("Cherry", 250, 0.05)]

    table = [f"{'Item':<10}{'Qty':>5}{'Price':>8}\n"]
    total_price = 0
    total_qty = 0

    for item, qty, price in rows:
        table.append(f"{item:<10}{qty:>5}{price:>8.2f}\n")
        total_price += qty * price
        total_qty += qty

    total = f"{'TOTAL':<10}{total_qty:>5}{total_price:>8.2f}\n"

    my_date = date(2024, 3, 15)

    return {
        "table": table,
        "total": total,
        "bases": [f"{255:b}", f"{255:o}", f"{255:x}", f"{255:#x}"],
        "day": f"{my_date:%d %B %Y}",
        "short": f"{'internationalization':.6}",
        "short": f"{'ab':->6}",
    }


if __name__ == "__main__":
    #     print("Problem 1 (f-strings):", problem_1())
    #     print("Problem 2 (format + %):", problem_2())
    print("Problem 3 (report table):", problem_3())
