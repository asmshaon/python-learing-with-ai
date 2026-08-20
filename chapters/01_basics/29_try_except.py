"""
Chapter 29: Python Try...Except
===============================

Notes
-----
- When something goes wrong Python RAISES an exception. If nobody catches it,
  the program stops and prints a traceback. try/except is how you catch one.
- The full shape has four parts, and they always run in this order:
      try:      the risky code
      except:   runs ONLY if a matching exception was raised
      else:     runs ONLY if the try block finished with no exception
      finally:  runs ALWAYS — success, failure, even on return
  else and finally are optional; you usually need try/except and finally.
- Catch the SPECIFIC exception, not everything:
      except ValueError:              one kind
      except (ValueError, TypeError): either kind, same handling
      except ValueError as err:       keep the object; str(err) is the message
  A bare "except:" also swallows Ctrl-C and SystemExit — never use it.
  "except Exception" is the widest sensible net: it catches ordinary errors but
  NOT KeyboardInterrupt / SystemExit, which inherit from BaseException instead.
- Order matters: several except blocks are tried top to bottom and the FIRST
  matching one wins, so list the specific classes before the general ones
  (ZeroDivisionError before ArithmeticError before Exception).
- Common built-ins: ValueError (right type, bad value), TypeError (wrong type),
  ZeroDivisionError, KeyError (missing dict key), IndexError (bad position),
  FileNotFoundError, AttributeError, KeyboardInterrupt.
- RAISING your own:
      raise ValueError("amount must be positive")
  Make a custom class by subclassing Exception, and give it attributes so the
  handler can inspect what happened:
      class InsufficientFunds(Exception):
          def __init__(self, balance, amount):
              super().__init__(f"balance {balance} is short of {amount}")
              self.balance = balance
              self.amount = amount
- CHAINING keeps the original cause visible in the traceback:
      raise RuntimeError("bad config") from err
  The new exception then carries err in its __cause__ attribute.
- A bare "raise" inside an except block RE-RAISES the exception you caught,
  unchanged — the way to log a problem and still let it travel upwards.
- finally is for CLEANUP that must happen either way (closing, releasing,
  restoring). Careful: a return inside finally overrides a return from try, and
  silently throws away any in-flight exception — a classic bug.
- Do not use exceptions to hide bugs. Catching an error and returning None is
  fine when you have a sensible fallback, harmful when it just delays the crash.

Run:  python3 chapters/01_basics/29_try_except.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Catching, and the order things run in
# Part A — write safe_divide(a, b) that returns a / b, or None when b is 0
#   (catch ZeroDivisionError). Test it with (10, 2) and (10, 0).
# Part B — write to_int(text) that returns int(text), or None on ValueError.
#   Test it with "42" and "abc".
# Part C — write run_steps(value) that appends the name of every block that
#   actually runs into a list: "try", "except", "else", "finally". Inside the
#   try it does 10 / value. Call it once with 2 (a clean run) and once with 0
#   (a failing run) and keep both lists.
# Part D — catch a TUPLE of exceptions: run int("x") and int(None) inside a
#   try that catches (ValueError, TypeError), and record the CLASS NAME of the
#   exception each one raised (use type(err).__name__).
# Part E — catch ZeroDivisionError from 1 / 0 as err and record str(err).
# Return a dict with keys:
#   "div_ok"        -> safe_divide(10, 2)
#   "div_zero"      -> safe_divide(10, 0)
#   "int_ok"        -> to_int("42")
#   "int_bad"       -> to_int("abc")
#   "success_log"   -> blocks that ran for the clean call
#   "failure_log"   -> blocks that ran for the failing call
#   "err_types"     -> the two class names from Part D
#   "zero_message"  -> the message string from Part E
# (Expected: {'div_ok': 5.0, 'div_zero': None, 'int_ok': 42, 'int_bad': None,
#             'success_log': ['try', 'else', 'finally'],
#             'failure_log': ['try', 'except', 'finally'],
#             'err_types': ['ValueError', 'TypeError'],
#             'zero_message': 'division by zero'})
# ---------------------------------------------------------------------------
from decimal import DivisionByZero
from math import e
from operator import call

from cycler import V
from matplotlib.pyplot import step


def safe_divide(a, b):
    if b == 0:
        return None

    return a / b


def to_int(val):
    try:
        return int(val)
    except ValueError:
        return None


def run_steps(value):
    steps = []

    try:
        steps.append("try")
        10 / value
    except:
        steps.append("except")
    else:
        steps.append("else")
    finally:
        steps.append("finally")

    return steps


def error_types(value):
    errors = []

    try:
        int(value)
    except ValueError:
        errors.append("ValueError")
    except TypeError:
        errors.append("TypeError")

    return errors


def div_zero(value):
    try:
        10 / value
    except ZeroDivisionError:
        return "division by zero"

    return None


def problem_1():

    nested = [error_types(r) for r in ["x", None]]

    return {
        "div_ok": safe_divide(10, 2),
        "div_zero": safe_divide(10, 0),
        "int_ok": to_int("42"),
        "int_bad": to_int("abc"),
        "success_log": run_steps(10),
        "failure_log": run_steps(0),
        "err_types": [error for errors in nested for error in errors],
        "zero_message": div_zero(0),
    }


# ---------------------------------------------------------------------------
# Problem 2: Raising your own errors
# Part A — define a custom exception class InsufficientFunds(Exception) that
#   takes balance and amount, builds a readable message, and stores both as
#   attributes.
# Part B — write withdraw(balance, amount) that:
#       raises ValueError if amount is 0 or negative,
#       raises InsufficientFunds if amount is bigger than balance,
#       otherwise returns the new balance.
# Part C — call it three ways and record what happened: (100, 30) succeeds;
#   (100, 500) is caught as InsufficientFunds — work out the SHORTFALL from the
#   attributes on the exception; (100, -5) is caught as ValueError — record the
#   class name.
# Part D — chaining: inside a try, do int("abc"), catch the ValueError as err,
#   and raise RuntimeError("bad config") from err. Catch that RuntimeError
#   outside and record its message plus the class name of its __cause__.
# Part E — re-raising: write a function that catches ZeroDivisionError from
#   1 / 0, appends "logged" to a list, then re-raises with a bare raise. Call
#   it inside a try and record the class name the OUTER handler sees.
# Return a dict with keys:
#   "ok"          -> the balance after the successful withdrawal
#   "shortfall"   -> how much more money was needed for the (100, 500) call
#   "bad_amount"  -> class name raised by the (100, -5) call
#   "wrapped"     -> the message of the RuntimeError from Part D
#   "cause"       -> class name of that RuntimeError's __cause__
#   "log"         -> the list the re-raising function wrote into
#   "reraised"    -> class name the outer handler caught in Part E
# (Expected: {'ok': 70, 'shortfall': 400, 'bad_amount': 'ValueError',
#             'wrapped': 'bad config', 'cause': 'ValueError',
#             'log': ['logged'], 'reraised': 'ZeroDivisionError'})
# ---------------------------------------------------------------------------
class InsufficientFunds(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(f"Insufficient funds: balance={balance}, amount={amount}")


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount can't be 0 or negetive")
    elif amount > balance:
        raise InsufficientFunds(balance=balance, amount=amount)
    else:
        return balance - amount


def runtime_error():
    try:
        int("abc")
    except ValueError as err:
        raise RuntimeError("bad config") from err


logs = []


def catch_zero_division():
    try:
        1 / 0
    except ZeroDivisionError:
        logs.append("logged")
        raise


def problem_2():

    ok = withdraw(100, 30)

    try:
        withdraw(100, 500)
    except InsufficientFunds as ex:
        shortfall = ex.amount - ex.balance

    try:
        withdraw(100, -5)
    except ValueError as e:
        bad_amount = type(e).__name__

    try:
        runtime_error()
    except RuntimeError as ex:
        wrapped = str(ex)
        caused = type(ex.__cause__).__name__

    try:
        catch_zero_division()
    except ZeroDivisionError as ex:
        reraised = type(ex).__name__

    return {
        "ok": ok,
        "shortfall": shortfall,
        "bad_amount": bad_amount,
        "wrapped": wrapped,
        "cause": caused,
        "log": logs,
        "reraised": reraised,
    }


# ---------------------------------------------------------------------------
# Problem 3: Cleanup, retries, and the traps
# Part A — simulate a resource: a list called events. Write use_resource(fail)
#   that appends "open", then raises RuntimeError("boom") if fail is True, and
#   appends "close" in a finally block. Call it both ways (catch the error on
#   the failing call) and keep the events list — "close" must appear both times.
# Part B — the finally trap: write a function whose try block returns "from
#   try" and whose finally block returns "from finally". Report which value the
#   caller actually gets.
# Part C — a retry loop: write a flaky function that fails with RuntimeError on
#   its first two calls and returns "ok" on the third (keep a counter in a list
#   or a default argument). Call it in a loop of at most 5 attempts, catching
#   the failures, and report the result plus how many attempts it took.
# Part D — write lookup(data, key) that returns data[key], catching KeyError to
#   return "missing". Test it on {"a": 1} with "a" and with "z".
# Part E — the Exception / BaseException line: inside a try, raise
#   KeyboardInterrupt. Give that try an "except Exception" block that would
#   record "caught by Exception", and wrap the whole thing in an outer
#   "except BaseException" that records "caught by BaseException". Report which
#   one actually ran.
# Return a dict with keys:
#   "events"        -> the event list from Part A
#   "finally_wins"  -> the value the caller got in Part B
#   "retry_result"  -> what the flaky function finally returned
#   "attempts"      -> how many calls that took
#   "found"         -> lookup on an existing key
#   "not_found"     -> lookup on a missing key
#   "caught_by"     -> which handler caught the KeyboardInterrupt
# (Expected: {'events': ['open', 'close', 'open', 'close'],
#             'finally_wins': 'from finally', 'retry_result': 'ok',
#             'attempts': 3, 'found': 1, 'not_found': 'missing',
#             'caught_by': 'caught by BaseException'})
# ---------------------------------------------------------------------------
events = []


def use_resource(fail):
    events.append("open")

    try:
        if fail:
            raise RuntimeError("boom")
    finally:
        events.append("close")


def trap():
    try:
        return "from try"
    finally:
        return "from finally"


calls = [0]


def flaky():
    calls[0] += 1

    if calls[0] < 3:
        raise RuntimeError("temporary failure")

    return "ok"


def lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return "missing"


def problem_3():
    for value in [True, False]:
        try:
            use_resource(value)
        except Exception:
            pass

    for _ in range(1, 6):
        try:
            final_result = flaky()
            break
        except RuntimeError:
            pass

    caught_by = None

    try:
        try:
            raise KeyboardInterrupt
        except Exception:
            caught_by = "Exception"
    except BaseException:
        caught_by = "BaseException"

    return {
        "events": events,
        "finally_wins": trap(),
        "retry_result": final_result,
        "attempts": calls[0],
        "found": lookup({"a": 1}, "a"),
        "not_found": lookup({"a": 1}, "b"),
        "caught_by": caught_by,
    }


if __name__ == "__main__":
    print("Problem 1 (catching):", problem_1())
    print("Problem 2 (raising):", problem_2())
    print("Problem 3 (cleanup):", problem_3())
