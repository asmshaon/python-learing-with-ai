"""
Chapter 24: Python Dates
========================

Notes
-----
- Dates are not a built-in type — they live in the datetime module:
      from datetime import date, time, datetime, timedelta
      date      year, month, day
      time      hour, minute, second, microsecond
      datetime  both halves together
      timedelta a LENGTH of time, not a point in time
- Making one:
      datetime(2024, 3, 15, 14, 30, 45)   built by hand
      date.today()                        today's date
      datetime.now()                      this moment
  Every piece is reachable as an attribute: d.year, d.month, d.day, d.hour,
  d.minute, d.second.
- weekday() gives 0 for Monday through 6 for Sunday. isoweekday() gives 1..7
  with Monday as 1.
- FORMATTING with strftime() turns a date into a string, using codes:
      %Y  4-digit year        %y  2-digit year
      %m  month as 01..12     %B  month name      %b  short month name
      %d  day as 01..31       %A  weekday name    %a  short weekday name
      %H  hour 00..23         %I  hour 01..12     %p  AM/PM
      %M  minute              %S  second          %j  day of the year
  Remember the direction: strFtime = FORMAT (date -> string).
- PARSING with strptime() goes the other way, string -> date, and you must tell
  it the shape of the string:
      datetime.strptime("15/03/2024", "%d/%m/%Y")
  strPtime = PARSE. A string that does not match the pattern raises ValueError.
- isoformat() gives the standard "2024-03-15T14:30:45" text, and
  date.fromisoformat() reads that shape back with no pattern needed.
- ARITHMETIC works naturally:
      one date MINUS another date  -> a timedelta
      a date PLUS a timedelta      -> another date
      a_timedelta.days             -> whole days as an int
  timedelta accepts days, hours, minutes, seconds, weeks. It does NOT accept
  months or years, because those have no fixed length.
- Dates compare with <, >, == like numbers do, so sorting a list of dates works.
- A datetime with no timezone attached is called NAIVE. Attaching one
  (timezone.utc) makes it AWARE. Never compare a naive one with an aware one.

Run:  python3 chapters/01_basics/24_dates.py
"""

from datetime import date, datetime, timedelta
import re


# ---------------------------------------------------------------------------
# Problem 1: Build a datetime and take it apart
# Build the exact moment 15 March 2024, 14:30:45, then report its pieces and a
# few formatted versions of it.
# Return a dict with keys:
#   "year"      -> the year
#   "month"     -> the month number
#   "day"       -> the day number
#   "hour"      -> the hour
#   "weekday"   -> weekday() as a number (Monday is 0)
#   "day_name"  -> the weekday's full name, via strftime
#   "iso"       -> isoformat()
#   "short"     -> formatted as "15/03/2024 14:30"
#   "wordy"     -> formatted as "Friday, 15 March 2024"
# (Expected: {'year': 2024, 'month': 3, 'day': 15, 'hour': 14, 'weekday': 4,
#             'day_name': 'Friday', 'iso': '2024-03-15T14:30:45',
#             'short': '15/03/2024 14:30',
#             'wordy': 'Friday, 15 March 2024'})
# ---------------------------------------------------------------------------
def problem_1():
    dt = datetime(2024, 3, 15, 14, 30, 45)

    return {
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
        "hour": dt.hour,
        "weekday": dt.weekday(),
        "day_name": dt.strftime("%A"),
        "iso": dt.isoformat(),
        "short": dt.strftime("%d/%m/%Y %H:%M"),
        "wordy": dt.strftime("%A, %d %B %Y"),
    }


# ---------------------------------------------------------------------------
# Problem 2: Parse strings and measure the gap between them
# You are given two dates written as text, in two DIFFERENT shapes:
#   start = "2024-01-01"        (year-month-day)
#   end   = "25/12/2024"        (day/month/year)
# Parse each one with strptime and the right pattern, then measure the distance
# between them. Also try to parse the broken string "31/02/2024" and catch the
# ValueError instead of letting it crash.
# Return a dict with keys:
#   "start"      -> the parsed start as a date, in isoformat() text
#   "end"        -> the parsed end as a date, in isoformat() text
#   "days"       -> whole days from start to end
#   "weeks"      -> those days as whole weeks (integer division)
#   "end_later"  -> True if end is after start
#   "bad_input"  -> True if parsing "31/02/2024" raised ValueError
# (Expected: {'start': '2024-01-01', 'end': '2024-12-25', 'days': 359,
#             'weeks': 51, 'end_later': True, 'bad_input': True})
# ---------------------------------------------------------------------------
from datetime import datetime


def problem_2(start="2024-01-01", end="25/12/2024"):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%d/%m/%Y")

    delta = end_date - start_date

    bad_input = False

    try:
        datetime.strptime("31/02/2024", "%d/%m/%Y")
    except ValueError:
        bad_input = True

    return {
        "start": start_date.date().isoformat(),
        "end": end_date.date().isoformat(),
        "days": delta.days,
        "weeks": delta.days // 7,
        "end_later": end_date > start_date,
        "bad_input": bad_input,
    }


# ---------------------------------------------------------------------------
# Problem 3: Date arithmetic with timedelta
# Work from the fixed date 15 March 2024 so the answers never change.
# Part A — add 30 days, and subtract 45 days.
# Part B — find the NEXT Monday strictly after that date (if the date itself is
#   a Monday, jump a full week). Use weekday() and a timedelta.
# Part C — find the last day of the month BEFORE it, by taking the first day of
#   its own month and stepping back one day. (2024 is a leap year, so this is a
#   good check.)
# Part D — work out someone's age in whole years on that date if they were born
#   on 20 July 1995. Remember to subtract one if their birthday has not happened
#   yet that year.
# Return a dict with isoformat() strings for the dates, and an int for the age:
#   "plus_30", "minus_45", "next_monday", "end_of_last_month", "age"
# (Expected: {'plus_30': '2024-04-14', 'minus_45': '2024-01-30',
#             'next_monday': '2024-03-18', 'end_of_last_month': '2024-02-29',
#             'age': 28})
# ---------------------------------------------------------------------------
from datetime import date, timedelta


def problem_3(today=date(2024, 3, 15), birthday=date(1995, 7, 20)):
    plus_30 = today + timedelta(days=30)
    minus_45 = today - timedelta(days=45)

    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7

    next_monday = today + timedelta(days=days_until_monday)

    end_of_last_month = today.replace(day=1) - timedelta(days=1)

    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return {
        "plus_30": plus_30.isoformat(),
        "minus_45": minus_45.isoformat(),
        "next_monday": next_monday.isoformat(),
        "end_of_last_month": end_of_last_month.isoformat(),
        "age": age,
    }


if __name__ == "__main__":
    print("Problem 1 (parts of a datetime):", problem_1())
    print("Problem 2 (parsing + gaps):", problem_2())
    print("Problem 3 (date arithmetic):", problem_3())
