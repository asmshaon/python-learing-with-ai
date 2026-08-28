"""
Chapter 01: Python File Handling
=================================

Notes
-----
- Python uses open() to access files: f = open("file.txt", mode).
- Common modes: "r" (read), "w" (write), "a" (append), "x" (create).
- Always close files with f.close() or use the 'with' statement.
- 'with' statement auto-closes the file when the block ends (preferred).
- File paths: relative ("data/file.txt") or absolute ("/home/user/file.txt").

Run:  python3 chapters/03_file_handling/01_file_handling.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Create a file with 'with' and confirm it was created
#   Input:  create "test1.txt" with content "hello"
#   Output: True (file exists)
# ---------------------------------------------------------------------------
import os


def problem_1():
    with open("test1.txt", "w") as file:
        file.write("hello")

    return os.path.exists("test1.txt")


# ---------------------------------------------------------------------------
# Problem 2: Open a file in different modes and return the mode behavior
#   Input:  write "data" to "test2.txt", then read it back
#   Output: "data"
# ---------------------------------------------------------------------------
def problem_2():
    with open("test2.txt", "w") as file:
        file.write("data")

    with open("test2.txt", "r") as file:
        content = file.read()

    return content


# ---------------------------------------------------------------------------
# Problem 3: Check if a file exists before opening it
#   Input:  safe_open("nonexistent.txt")
#   Output: "File not found"
# ---------------------------------------------------------------------------


def safe_open(filename):
    if not os.path.exists(filename):
        return "File not found"

    with open(filename, "r") as file:
        return file.read()


def problem_3():
    return safe_open("ddd.txt")


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
