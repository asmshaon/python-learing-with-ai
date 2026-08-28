"""
Chapter 04: Python Delete Files
================================

Notes
-----
- import os to use file system operations.
- os.remove("file.txt") deletes a single file — raises FileNotFoundError if missing.
- os.rmdir("dir") removes an empty directory.
- shutil.rmtree("dir") removes a directory and all its contents.
- Always check if a file exists before deleting to avoid errors.

Run:  python3 chapters/03_file_handling/04_delete_files.py
"""

# ---------------------------------------------------------------------------
# Problem 1: Delete a file and confirm it is gone
#   Input:  create "temp.txt", delete it, check exists
#   Output: False
# ---------------------------------------------------------------------------
import os


def problem_1():
    with open("temp.txt", "w") as file:
        pass

    if os.path.exists("temp.txt"):
        os.remove("temp.txt")

    return os.path.exists("temp.txt")


# ---------------------------------------------------------------------------
# Problem 2: Safely delete a file (no error if already gone)
#   Input:  safe_delete("ghost.txt") -> "Deleted or never existed"
#   Output: "Deleted or never existed"
# ---------------------------------------------------------------------------


def safe_delete(filename):
    try:
        os.remove(filename)
        return True
    except FileNotFoundError:
        pass

    return "Deleted or never existed"


def problem_2():
    return safe_delete("axy.txt")


# ---------------------------------------------------------------------------
# Problem 3: Delete an empty directory
#   Input:  create "empty_dir/", delete it, check exists
#   Output: False
# ---------------------------------------------------------------------------
def problem_3():
    os.mkdir("empty_dir")

    os.rmdir("empty_dir")

    return os.path.exists("empty_dir")


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
