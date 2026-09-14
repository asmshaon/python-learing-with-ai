"""
Chapter 01: NumPy Tutorial
============================

Notes
-----
- NumPy is the core library for numerical computing in Python.
- Install: pip install numpy
- Import: import numpy as np
- ndarray is the main data structure — fast, fixed-type, fixed-size array.
- Create arrays: np.array([1,2,3]), np.zeros((2,3)), np.ones((3,)), np.arange(0,10,2).
- Vectorized operations: no need for loops — np.array([1,2,3]) * 2 gives [2,4,6].
- Slicing works like lists: arr[1:3], arr[:, 0].

Run:  python3 chapters/04_libraries/01_numpy_tutorial.py
"""

# pip install numpy

# ---------------------------------------------------------------------------
# Problem 1: Create a NumPy array and compute the sum
#   Input:  np.array([10, 20, 30, 40, 50])
#   Output: 150
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Reshape a 1D array into a 2D matrix
#   Input:  np.arange(1, 7).reshape(2, 3)
#   Output: [[1, 2, 3], [4, 5, 6]]
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Filter elements from an array using boolean indexing
#   Input:  arr = np.array([5, 12, 3, 18, 7, 20]), filter arr > 10
#   Output: [12, 18, 20]
# ---------------------------------------------------------------------------
def problem_3():
    pass


# ---------------------------------------------------------------------------
# Problem 4: Create an array of zeros with a specific shape
#   Input:  np.zeros((3, 4))
#   Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# ---------------------------------------------------------------------------
def problem_4():
    pass


# ---------------------------------------------------------------------------
# Problem 5: Create an array of ones with a specific shape
#   Input:  np.ones((2, 5))
#   Output: [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# ---------------------------------------------------------------------------
def problem_5():
    pass


# ---------------------------------------------------------------------------
# Problem 6: Generate evenly spaced values using arange
#   Input:  np.arange(0, 20, 5)
#   Output: [0, 5, 10, 15]
# ---------------------------------------------------------------------------
def problem_6():
    pass


# ---------------------------------------------------------------------------
# Problem 7: Generate linearly spaced values using linspace
#   Input:  np.linspace(0, 1, 5)
#   Output: [0.0, 0.25, 0.5, 0.75, 1.0]
# ---------------------------------------------------------------------------
def problem_7():
    pass


# ---------------------------------------------------------------------------
# Problem 8: Compute element-wise addition of two arrays
#   Input:  np.array([1, 2, 3]) + np.array([4, 5, 6])
#   Output: [5, 7, 9]
# ---------------------------------------------------------------------------
def problem_8():
    pass


# ---------------------------------------------------------------------------
# Problem 9: Multiply every element in an array by a scalar
#   Input:  np.array([2, 4, 6]) * 3
#   Output: [6, 12, 18]
# ---------------------------------------------------------------------------
def problem_9():
    pass


# ---------------------------------------------------------------------------
# Problem 10: Find the maximum and minimum of an array
#   Input:  np.array([3, 7, 1, 9, 4])
#   Output: max=9, min=1
# ---------------------------------------------------------------------------
def problem_10():
    pass


# ---------------------------------------------------------------------------
# Problem 11: Find the index of the maximum element
#   Input:  np.array([10, 50, 30, 20, 40])
#   Output: 1
# ---------------------------------------------------------------------------
def problem_11():
    pass


# ---------------------------------------------------------------------------
# Problem 12: Compute the mean of an array
#   Input:  np.array([10, 20, 30, 40, 50])
#   Output: 30.0
# ---------------------------------------------------------------------------
def problem_12():
    pass


# ---------------------------------------------------------------------------
# Problem 13: Compute the standard deviation of an array
#   Input:  np.array([10, 20, 30, 40, 50])
#   Output: 14.1421...
# ---------------------------------------------------------------------------
def problem_13():
    pass


# ---------------------------------------------------------------------------
# Problem 14: Sort an array in ascending order
#   Input:  np.array([5, 2, 8, 1, 9])
#   Output: [1, 2, 5, 8, 9]
# ---------------------------------------------------------------------------
def problem_14():
    pass


# ---------------------------------------------------------------------------
# Problem 15: Reverse an array
#   Input:  np.array([1, 2, 3, 4, 5])
#   Output: [5, 4, 3, 2, 1]
# ---------------------------------------------------------------------------
def problem_15():
    pass


# ---------------------------------------------------------------------------
# Problem 16: Concatenate two arrays
#   Input:  np.array([1, 2, 3]) and np.array([4, 5, 6])
#   Output: [1, 2, 3, 4, 5, 6]
# ---------------------------------------------------------------------------
def problem_16():
    pass


# ---------------------------------------------------------------------------
# Problem 17: Reshape a 1D array into a column vector
#   Input:  np.array([1, 2, 3, 4]).reshape(4, 1)
#   Output: [[1], [2], [3], [4]]
# ---------------------------------------------------------------------------
def problem_17():
    pass


# ---------------------------------------------------------------------------
# Problem 18: Compute dot product of two arrays
#   Input:  np.array([1, 2, 3]) and np.array([4, 5, 6])
#   Output: 32
# ---------------------------------------------------------------------------
def problem_18():
    pass


# ---------------------------------------------------------------------------
# Problem 19: Replace all negative values with zero
#   Input:  np.array([3, -1, 4, -2, 5])
#   Output: [3, 0, 4, 0, 5]
# ---------------------------------------------------------------------------
def problem_19():
    pass


# ---------------------------------------------------------------------------
# Problem 20: Create an identity matrix of size 4x4
#   Input:  np.eye(4)
#   Output: [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
# ---------------------------------------------------------------------------
def problem_20():
    pass


# ---------------------------------------------------------------------------
# Problem 21: Matrix multiplication of two 2D arrays
#   Input:  np.array([[1,2],[3,4]]) @ np.array([[5,6],[7,8]])
#   Output: [[19, 22], [43, 50]]
# ---------------------------------------------------------------------------
def problem_21():
    pass


# ---------------------------------------------------------------------------
# Problem 22: Find unique elements in an array
#   Input:  np.array([1, 2, 2, 3, 3, 3, 4])
#   Output: [1, 2, 3, 4]
# ---------------------------------------------------------------------------
def problem_22():
    pass


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
    print("Problem 4:", problem_4())
    print("Problem 5:", problem_5())
    print("Problem 6:", problem_6())
    print("Problem 7:", problem_7())
    print("Problem 8:", problem_8())
    print("Problem 9:", problem_9())
    print("Problem 10:", problem_10())
    print("Problem 11:", problem_11())
    print("Problem 12:", problem_12())
    print("Problem 13:", problem_13())
    print("Problem 14:", problem_14())
    print("Problem 15:", problem_15())
    print("Problem 16:", problem_16())
    print("Problem 17:", problem_17())
    print("Problem 18:", problem_18())
    print("Problem 19:", problem_19())
    print("Problem 20:", problem_20())
    print("Problem 21:", problem_21())
    print("Problem 22:", problem_22())
