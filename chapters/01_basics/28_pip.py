"""
Chapter 28: Python PIP
======================

Notes
-----
- pip is Python's PACKAGE INSTALLER. It downloads packages from PyPI
  (the Python Package Index, pypi.org) and puts them where import can find them.
- The standard library ships with Python; everything else comes from pip.
- Always call it through the interpreter you actually use, so the package lands
  in the right environment:
      python3 -m pip install requests
  Plain "pip install requests" can belong to a different Python.
- The commands worth remembering:
      python3 -m pip install rich          install the latest version
      python3 -m pip install rich==13.7.0  install one exact version
      python3 -m pip install -U rich       upgrade
      python3 -m pip uninstall rich        remove
      python3 -m pip list                  everything installed here
      python3 -m pip show rich             version, location, dependencies
      python3 -m pip freeze                installed packages as pinned lines
      python3 -m pip install -r requirements.txt   install a whole file
- VERSION SPECIFIERS decide how much freedom pip has:
      rich==13.7.0   exactly this          rich>=13        this or newer
      rich>=13,<14   a range               rich~=13.7.0    13.7.x, no 13.8
      rich           whatever is newest
  Pinning (==) makes a build repeatable; ranges pick up bug fixes.
- requirements.txt is just a text file, one requirement per line. Blank lines
  are skipped, a line starting with # is a comment, # after a requirement is an
  inline comment, and a line starting with - is an option (like -r other.txt).
  Create it with: python3 -m pip freeze > requirements.txt
- Install into a VIRTUAL ENVIRONMENT, never system-wide, so one project's
  versions cannot break another's:
      python3 -m venv .venv && source .venv/bin/activate
  Inside a venv, sys.prefix differs from sys.base_prefix — that is how a
  program can tell it is running in one.
- From inside Python, do NOT import pip and call it. pip is a command line
  tool. To INSPECT what is installed, use the standard library instead:
      from importlib.metadata import version, metadata, distributions
      version("pip")                  -> "24.0"
      metadata("pip")["Summary"]      -> the one-line description
      distributions()                 -> an iterator over everything installed
  version() raises importlib.metadata.PackageNotFoundError when the package is
  not installed — that is the clean way to check for one.
- To RUN a pip command from Python, shell out with subprocess and sys.executable:
      subprocess.run([sys.executable, "-m", "pip", "--version"],
                     capture_output=True, text=True)
  The result has .returncode (0 means success), .stdout and .stderr.

Run:  python3 chapters/01_basics/28_pip.py
"""

from ast import operator
import importlib
import importlib.util
import re
import subprocess
import sys
from importlib.metadata import PackageNotFoundError, distributions, metadata, version

from numpy.char import strip


# ---------------------------------------------------------------------------
# Problem 1: Inspect the environment you are installing into
# Part A — report whether this Python is running inside a virtual environment
#   (compare sys.prefix with sys.base_prefix).
# Part B — report the installed version of pip itself as a string.
# Part C — write a small helper is_installed(name) that returns True/False by
#   calling version() and catching PackageNotFoundError. Test it with "pip"
#   and with "totally-not-a-real-package".
# Part D — report the one-line Summary from pip's own metadata.
# Part E — count how many distributions are installed in this environment.
# Return a dict with keys:
#   "in_venv"        -> True/False
#   "pip_version"    -> the version string
#   "pip_installed"  -> True/False for "pip"
#   "fake_installed" -> True/False for "totally-not-a-real-package"
#   "pip_summary"    -> the Summary string from pip's metadata
#   "package_count"  -> how many distributions are installed
# (Values depend on YOUR machine. Expected shape: in_venv/pip_installed/
#  fake_installed are booleans — the fake one must be False, "pip" must be
#  True; pip_version and pip_summary are non-empty strings; package_count is
#  an int of at least 1.)
# ---------------------------------------------------------------------------
def problem_1():
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--format=freeze"],
        capture_output=True,
        text=True,
    )

    count = len(result.stdout.strip().splitlines())

    try:
        fake_installed = version("pip")
        fake_installed = True
    except PackageNotFoundError:
        fake_installed = False

    return {
        "in_venv": sys.prefix is not sys.base_prefix,
        "pip_version": version("pip"),
        "pip_installed": importlib.util.find_spec("pip") is not None,
        "fake_installed": fake_installed,
        "pip_summary": metadata("pip")["Summary"],
        "package_count": count,
    }


# ---------------------------------------------------------------------------
# Problem 2: Read a requirements.txt by hand
# Work on this text (a real requirements file, warts and all):
#   req_text = (
#       "# core deps\n"
#       "requests==2.31.0\n"
#       "flask>=2.0\n"
#       "\n"
#       "numpy~=1.26.0\n"
#       "pytest    # test runner\n"
#       "-r other.txt\n"
#       "rich>=13,<14\n"
#   )
# Part A — clean it: split into lines, drop blank lines, drop full comment
#   lines, drop option lines starting with "-", and strip any inline comment
#   (everything from a # onwards) plus surrounding whitespace.
# Part B — from each cleaned line, split the package NAME from its SPECIFIER.
#   The name is everything before the first of the characters = < > ~ !
#   (a line with no specifier is all name, and its specifier is "").
# Part C — list just the names.
# Part D — list the names that are PINNED to one exact version (they use ==).
# Part E — build a dict of name -> specifier.
# Return a dict with keys:
#   "cleaned" -> the cleaned requirement lines
#   "names"   -> list of package names
#   "pinned"  -> names pinned with ==
#   "specs"   -> dict of name -> specifier
# (Expected: {'cleaned': ['requests==2.31.0', 'flask>=2.0', 'numpy~=1.26.0',
#                         'pytest', 'rich>=13,<14'],
#             'names': ['requests', 'flask', 'numpy', 'pytest', 'rich'],
#             'pinned': ['requests'],
#             'specs': {'requests': '==2.31.0', 'flask': '>=2.0',
#                       'numpy': '~=1.26.0', 'pytest': '',
#                       'rich': '>=13,<14'}})
# ---------------------------------------------------------------------------
def problem_2():
    req_text = (
        "# core deps\n"
        "requests==2.31.0\n"
        "flask>=2.0\n"
        "\n"
        " numpy~=1.26.0\n"
        "pytest    # test runner\n"
        "-r other.txt\n"
        "rich>=13,<14\n"
    )

    cleaned = []
    names = []
    pinned = []
    match_dict = []

    for l in req_text.split("\n"):
        if l != "" and l.startswith("-r") == False:
            v = l.split("#", 1)[0]
            v = v.strip()

            if v.strip() != "":
                cleaned.append(v)

                names.append(re.split(r"[=<>~!]", v, maxsplit=1)[0].strip())

                if "==" in v:
                    pinned.append(v.split("=", 1)[0].strip())

                match = re.match(r"^([a-z]+)([=<>~!])(.*)$", v)

                if match:
                    name = match.group(1)
                    operator = match.group(2) or ""
                    version = match.group(3)

                    specified = f"{operator}{version}" if operator else ""

                    match_dict.append((name, specified))
                else:
                    match_dict.append((v, ""))

    return {
        "cleaned": cleaned,
        "names": names,
        "pinned": pinned,
        "specs": dict(match_dict),
    }


# ---------------------------------------------------------------------------
# Problem 3: Drive pip from Python, and check dependencies
# Part A — run "python3 -m pip --version" with subprocess (use sys.executable,
#   capture_output=True, text=True) and report the return code.
# Part B — pull the version NUMBER out of that output. The line looks like
#   "pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)", so the
#   number is the second whitespace-separated piece.
# Part C — write a helper missing_packages(wanted) that returns the names from
#   the list that are NOT installed. Run it on
#   ["pip", "totally-not-a-real-package"].
# Part D — build the freeze-style pinned line for pip, in the shape
#   "pip==<version>", using the version you already looked up in Problem 1.
# Part E — report the install COMMAND a user would run to reproduce that exact
#   version, as the list of arguments you would hand to subprocess.
# Return a dict with keys:
#   "returncode"   -> 0 if the pip command succeeded
#   "cli_version"  -> version number parsed out of the command output
#   "missing"      -> the not-installed names from Part C
#   "freeze_line"  -> "pip==<version>"
#   "install_cmd"  -> [sys.executable, "-m", "pip", "install", "<freeze_line>"]
# (Expected: returncode 0; cli_version a string like "24.0" that matches the
#  version from Problem 1; missing == ['totally-not-a-real-package'];
#  freeze_line starting with "pip=="; install_cmd a 5-item list.)
# ---------------------------------------------------------------------------
def problem_3():
    result = subprocess.run(
        [sys.executable, "-m" "pip", "--version"],
        capture_output=True,
        text=True,
    )

    returncode = result.returncode

    return {
        "returncode": returncode,
        "cli_version": result.stdout.split()[1],
        "missing": [
            name
            for name in ["pip", "totally-not-a-real-package"]
            if importlib.util.find_spec(name) is None
        ],
        "freeze_line": f"pip=={version('pip')}",
        "install_cmd": [
            sys.executable,
            "-m",
            "pip",
            "install",
            f"pip=={version('pip')}",
        ],
    }


if __name__ == "__main__":
    print("Problem 1 (environment):", problem_1())
    print("Problem 2 (requirements):", problem_2())
    print("Problem 3 (running pip):", problem_3())
