"""
Chapter 03: Python Write/Create Files
======================================

Notes
-----
- open("file.txt", "w") creates or overwrites a file.
- open("file.txt", "a") appends to an existing file without overwriting.
- open("file.txt", "x") creates a new file — raises error if it already exists.
- f.write("text") writes a string to the file.
- f.writelines(["line1\n", "line2\n"]) writes a list of strings.
- Always use 'with' to ensure data is flushed and file is closed.

Run:  python3 chapters/03_file_handling/03_write_files.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Write a string to a file and read it back
#   Input:  write "Hello, File!" to "output.txt", then read
#   Output: "Hello, File!"
# ---------------------------------------------------------------------------
import os


def problem_1():
    with open("abc.txt", "w") as file:
        file.write("Hello, File!")

    with open("abc.txt", "r") as file:
        return file.read()


# ---------------------------------------------------------------------------
# Problem 2: Append multiple lines to a file
#   Input:  append ["line1\n", "line2\n"] to "log.txt"
#   Output: ["line1", "line2"]
# ---------------------------------------------------------------------------
def problem_2():

    with open("axy.txt", "a") as file:
        for line in ["line1\n", "line2\n"]:
            file.write(line)

    with open("axy.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


# ---------------------------------------------------------------------------
# Problem 3: Create a file only if it does not already exist
#   Input:  create_safe("new.txt") -> True
#           create_safe("new.txt") -> "File already exists"
#   Output: True, "File already exists"
# ---------------------------------------------------------------------------


def create_safe(filename):
    try:
        with open(filename, "x") as file:
            return True
    except FileExistsError:
        return "File already exists"


def problem_3():
    return create_safe("new2.txt")


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
