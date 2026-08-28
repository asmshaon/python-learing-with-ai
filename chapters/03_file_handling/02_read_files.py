"""
Chapter 02: Python Read Files
==============================

Notes
-----
- f.read() reads the entire file as a single string.
- f.readline() reads one line at a time.
- f.readlines() returns a list of all lines.
- Use 'with open(...) as f:' to safely read and auto-close.
- Strip trailing newlines with .strip() when processing lines.

Run:  python3 chapters/03_file_handling/02_read_files.py
"""


# ---------------------------------------------------------------------------
# Problem 1: Read entire file content as a string
#   Input:  file "sample.txt" contains "Hello\nWorld"
#   Output: "Hello\nWorld"
# ---------------------------------------------------------------------------
def problem_1():
    with open("test1.txt", "r") as file:
        content = file.read()

    return content


# ---------------------------------------------------------------------------
# Problem 2: Read file line by line and return as a list
#   Input:  file "lines.txt" contains "one\ntwo\nthree"
#   Output: ["one", "two", "three"]
# ---------------------------------------------------------------------------
def problem_2():
    with open("test1.txt", "r") as file:
        return [line.strip() for line in file.read().split()]


# ---------------------------------------------------------------------------
# Problem 3: Count the number of words in a file
#   Input:  file "words.txt" contains "I love Python"
#   Output: 3
# ---------------------------------------------------------------------------
def problem_3():
    with open("test1.txt", "r") as file:
        return len(file.read().split())


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
