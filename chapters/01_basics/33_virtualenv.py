r"""
Chapter 33: Python VirtualEnv
=============================

Notes
-----
- A virtual environment (venv) is a FOLDER that holds its own Python binary and
  its own installed packages. It isolates one project's dependencies from the
  system Python and from every other project. Create it with:
      python3 -m venv .venv
  `venv` is a STANDARD LIBRARY module — nothing to pip install. The folder
  name (.venv, venv, env) is just convention; put it anywhere.
- ACTIVATION makes the shell use the environment's python/pip without typing
  the full path. It differs per shell and is NOT part of Python itself:
      source .venv/bin/activate          bash / zsh
      source .venv/bin/activate.fish     fish
      .venv\Scripts\activate             Windows (cmd / PowerShell)
  While active, the shell prompt usually shows the env name, and `python` and
  `pip` now point inside .venv/. Leave it with:  deactivate
- You do NOT need to activate to use the env — you can always call the binaries
  by their absolute path:
      .venv/bin/python -m pip install requests
      .venv/bin/python script.py
- HOW TO TELL you are inside one, from Python:
      sys.prefix            -> where this interpreter lives (the venv when active)
      sys.base_prefix       -> the base interpreter it was created from
      in a venv:  sys.prefix != sys.base_prefix
      os.environ.get("VIRTUAL_ENV") -> the venv path when ACTIVATED (unset when
                                       calling the binary by path)
      sys.executable        -> the full path of the running interpreter
- The venv's own layout (created by the module):
      .venv/bin/            python3, pip (and the activate scripts)
      .venv/lib/python3.12/ site-packages/ where packages land
      .venv/include/        build headers
      .venv/pyvenv.cfg      a tiny INI file: home, version, include-system-site
- pyvenv.cfg sets the rules: "include-system-site-packages = false" keeps the
  venv isolated (the default); set true to ALSO see system packages.
- REPRODUCIBILITY is the whole point of a venv:
      .venv/bin/pip freeze > requirements.txt     snapshot exact versions
      pip install -r requirements.txt             rebuild them elsewhere
- A venv is disposable: it contains no project code, just environment. Delete
  the folder to remove it, and DO NOT commit it — add ".venv/" to .gitignore.
- Version warnings: if multiple Pythons exist, `python3 -m venv` uses whatever
  python3 resolves to; pin it with `python3.12 -m venv .venv` for a specific one.

Run:  python3 chapters/01_basics/33_virtualenv.py
"""

import os
import sys


# ---------------------------------------------------------------------------
# Problem 1: Inspect the environment you are running in
# Part A — report whether the CURRENT interpreter looks like a venv: is
#   sys.prefix different from sys.base_prefix? Is the VIRTUAL_ENV variable set?
#   What is sys.prefix?
# Part B — report where the interpreter would find its python3 executable
#   (sys.executable) and the site-packages folder it would install into —
#   sys.prefix + "/lib/pythonX.Y/site-packages" where X.Y comes from
#   sys.version_info. Build the path with os.path.join, NOT string "+".
# Part C — simulate the venv CHECK you would do before running commands: write
#   a helper is_like_venv(prefix, base) that returns True only when the two
#   paths differ. Test it with ("/proj/.venv", "/usr") -> True and
#   ("/usr", "/usr") -> False.
# Part D — report the python version triplet (major, minor, micro) as a string
#   like "3.12.x", reading it from sys.version_info.
# Return a dict with keys:
#   "prefix_differs" -> True/False: sys.prefix != sys.base_prefix
#   "virtual_env_set"-> True/False: os.environ.get("VIRTUAL_ENV") is set
#   "prefix"         -> sys.prefix
#   "executable"     -> sys.executable
#   "site_packages"  -> the computed site-packages path
#   "sim_venv"       -> is_like_venv("/proj/.venv", "/usr")
#   "sim_system"     -> is_like_venv("/usr", "/usr")
#   "version"        -> "3.12.x" style string
# (Values depend on YOUR machine. Expected shape: prefix_differs is True when
#  running inside an activated venv and False otherwise; virtual_env_set matches
#  that; site_packages ends in "/site-packages"; sim_venv True, sim_system
#  False; version starts with the major.minor Python you run.)
# ---------------------------------------------------------------------------
def is_like_venv(prefix, base):
    return prefix != base


def problem_1():
    return {
        "prefix_differs": sys.prefix != sys.base_prefix,
        "virtual_env_set": (os.environ.get("VIRTUAL_ENV") is not None),
        "prefix": sys.prefix,
        "executable": sys.executable,
        "site_packages": os.path.join(
            sys.prefix,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            "site-packages",
        ),
        "sim_venv": is_like_venv("/proj/.venv", "/usr"),
        "sim_system": is_like_venv("/usr", "/usr"),
        "version": (
            f"{sys.version_info.major}."
            f"{sys.version_info.minor}."
            f"{sys.version_info.micro}"
        ),
    }


# ---------------------------------------------------------------------------
# Problem 2: The commands you would actually type
# Build the COMMAND LINES a developer needs, as strings, plus a tiny simulation
# of what activation does to the environment.
# Part A — create_env(dir) -> the list you would hand to subprocess to create a
#   venv at dir: [sys.executable, "-m", "venv", dir].
# Part B — bin_paths(dir) -> the paths that must exist inside a fresh venv so
#   you can call it without activating: <dir>/bin/python3 and <dir>/bin/pip.
#   Build them with os.path.join. (Do not actually create files — just return
#   the paths.)
# Part C — cfg_line() -> the pyvenv.cfg line that keeps the venv isolated:
#   "include-system-site-packages = false". Return it as the exact string.
# Part D — freeze_cmd(env_dir) -> the list to snapshot installed versions:
#   [<env_dir>/bin/pip, "freeze"]. And install_cmd(env_dir, req_file) ->
#   [<env_dir>/bin/pip, "install", "-r", req_file].
# Part E — simulate activation: write activate_like(prefix, base) that returns
#   the dict {"prefix": prefix, "base": base} — i.e. after activation the
#   interpreter points INTO the venv while the base stays the system python.
# Return a dict with keys:
#   "create"    -> the venv creation command list
#   "python_bin"-> <dir>/bin/python3 for dir "proj/.venv"
#   "pip_bin"   -> <dir>/bin/pip for dir "proj/.venv"
#   "isolated"  -> the exact pyvenv.cfg line
#   "freeze"    -> the pip freeze command list
#   "install"   -> the pip install -r command list
#   "activated" -> activate_like("/proj/.venv", "/usr")
# (Expected: {'create': ['/usr/bin/python3', '-m', 'venv', '.venv'],
#             'python_bin': 'proj/.venv/bin/python3',
#             'pip_bin': 'proj/.venv/bin/pip',
#             'isolated': 'include-system-site-packages = false',
#             'freeze': ['proj/.venv/bin/pip', 'freeze'],
#             'install': ['proj/.venv/bin/pip', 'install', '-r', 'requirements.txt'],
#             'activated': {'prefix': '/proj/.venv', 'base': '/usr'}})
#  (The exact path in "create" depends on your sys.executable.)
# ---------------------------------------------------------------------------
def problem_2():
    dir = "proj/.venv"
    return {
        "create": [sys.executable, "-m", "venv", ".venv"],
        "python_bin": os.path.join(dir, "bin", "python3"),
        "pip_bin": os.path.join(dir, "bin", "pip"),
        "isolated": "include-system-site-packages = false",
        "freeze": [os.path.join(dir, "bin", "pip"), "freeze"],
        "install": [
            os.path.join(dir, "bin", "pip"),
            "install",
            "-r",
            "requirements.txt",
        ],
        "activated": {"prefix": "/proj/.venv", "base": "/usr"},
    }


# ---------------------------------------------------------------------------
# Problem 3: A reproducibility workflow, end to end
# Part A — write parse_freeze(text) that turns a `pip freeze` blob into a dict
#   of package -> version. Each line looks like "requests==2.31.0"; a line with
#   no "==" (e.g. "# editable installs") is skipped; the version is everything
#   after the FIRST "==". Also strip trailing whitespace per line.
# Part B — write pin(mapping) that returns the sorted list of "name==version"
#   lines — the exact content pip freeze would have produced from that mapping.
# Part C — write installed(mapping, wanted) that, given a frozen mapping and a
#   list of wanted names, returns the names from `wanted` that are NOT in the
#   mapping (what `pip install -r` would still have to install).
# Part D — write activate_prompt(env_name) that returns the bash line to
#   activate a venv named env_name: "source <env_name>/bin/activate", and
#   deactivate_prompt() returning the plain "deactivate".
# Part E — write gitignore_line() returning the line you would add to .gitignore
#   so a venv folder named ".venv" is never committed: ".venv/".
# Return a dict with keys:
#   "frozen"      -> parse_freeze of the blob below
#   "pinned"      -> pin({"rich": "13.7.0", "numpy": "1.26.0"})
#   "still_missing"-> installed({"requests": "2.31.0"}, ["rich", "requests"])
#   "activate"    -> the bash activation line for ".venv"
#   "deactivate"  -> "deactivate"
#   "gitignore"   -> the .gitignore line
# (Expected: {'frozen': {'requests': '2.31.0', 'rich': '13.7.0',
#                        'numpy': '1.26.0'},
#             'pinned': ['numpy==1.26.0', 'rich==13.7.0'],
#             'still_missing': ['rich'], 'activate': 'source .venv/bin/activate',
#             'deactivate': 'deactivate', 'gitignore': '.venv/'})
# ---------------------------------------------------------------------------
def problem_3():
    freeze_blob = """
# This is a comment line
requests==2.31.0
rich==13.7.0
numpy==1.26.0
# Another comment
"""

    def parse_freeze(text):
        mapping = {}
        for line in text.strip().splitlines():
            line = line.strip()
            if "==" in line:
                name, version = line.split("==", 1)
                mapping[name] = version
        return mapping

    def pin(mapping):
        return sorted(f"{name}=={version}" for name, version in mapping.items())

    def installed(frozen, wanted):
        return [name for name in wanted if name not in frozen]

    def activate_prompt(env_name):
        return f"source {env_name}/bin/activate"

    def deactivate_prompt():
        return "deactivate"

    def gitignore_line():
        return ".venv/"

    return {
        "frozen": parse_freeze(freeze_blob),
        "pinned": pin({"rich": "13.7.0", "numpy": "1.26.0"}),
        "still_missing": installed({"requests": "2.31.0"}, ["rich", "requests"]),
        "activate": activate_prompt(".venv"),
        "deactivate": deactivate_prompt(),
        "gitignore": gitignore_line(),
    }


if __name__ == "__main__":
    print("Problem 1 (inspect):", problem_1())
    print("Problem 2 (commands):", problem_2())
    print("Problem 3 (workflow):", problem_3())
