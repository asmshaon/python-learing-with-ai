"""
Chapter 03: SciPy Tutorial
============================

Notes
-----
- SciPy builds on NumPy for scientific and technical computing.
- Install: pip install scipy
- Key modules: scipy.stats, scipy.optimize, scipy.spatial, scipy.linalg.
- scipy.stats provides statistical functions: mean, median, mode, std, etc.
- scipy.optimize offers minimization and curve fitting.
- scipy.spatial includes distance computations and KD-trees.

Run:  python3 chapters/04_libraries/03_scipy_tutorial.py
"""

# pip install scipy

# ---------------------------------------------------------------------------
# Problem 1: Calculate mean using scipy.stats
#   Input:  [10, 20, 30, 40, 50]
#   Output: 30.0
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Calculate standard deviation
#   Input:  [10, 20, 30, 40, 50]
#   Output: 14.1421...
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Find the mode of a dataset
#   Input:  [1, 2, 2, 3, 3, 3, 4]
#   Output: mode=3
# ---------------------------------------------------------------------------
def problem_3():
    pass


# ---------------------------------------------------------------------------
# Problem 4: Compute Euclidean distance between two points
#   Input:  point1=(1, 2), point2=(4, 6)
#   Output: 5.0
# ---------------------------------------------------------------------------
def problem_4():
    pass


# ---------------------------------------------------------------------------
# Problem 5: Calculate median of a dataset
#   Input:  [7, 3, 1, 5, 9]
#   Output: 5
# ---------------------------------------------------------------------------
def problem_5():
    pass


# ---------------------------------------------------------------------------
# Problem 6: Compute variance of a dataset
#   Input:  [2, 4, 4, 4, 5, 5, 7, 9]
#   Output: 4.0
# ---------------------------------------------------------------------------
def problem_6():
    pass


# ---------------------------------------------------------------------------
# Problem 7: Compute correlation coefficient between two arrays
#   Input:  x=[1,2,3,4,5], y=[2,4,6,8,10]
#   Output: 1.0
# ---------------------------------------------------------------------------
def problem_7():
    pass


# ---------------------------------------------------------------------------
# Problem 8: Perform a t-test on two samples
#   Input:  sample1=[5,6,7,8,9], sample2=[1,2,3,4,5]
#   Output: t-statistic > 0 (significant difference)
# ---------------------------------------------------------------------------
def problem_8():
    pass


# ---------------------------------------------------------------------------
# Problem 9: Generate a normal distribution
#   Input:  mean=0, std=1, size=5
#   Output: 5 random values from N(0,1)
# ---------------------------------------------------------------------------
def problem_9():
    pass


# ---------------------------------------------------------------------------
# Problem 10: Compute the CDF of a normal distribution
#   Input:  x=0, loc=0, scale=1
#   Output: 0.5
# ---------------------------------------------------------------------------
def problem_10():
    pass


# ---------------------------------------------------------------------------
# Problem 11: Perform linear regression (linregress)
#   Input:  x=[1,2,3,4,5], y=[2,4,5,4,5]
#   Output: slope, intercept, r_value
# ---------------------------------------------------------------------------
def problem_11():
    pass


# ---------------------------------------------------------------------------
# Problem 12: Find the minimum of a function using minimize
#   Input:  f(x) = (x-3)^2, start at x=0
#   Output: x=3.0
# ---------------------------------------------------------------------------
def problem_12():
    pass


# ---------------------------------------------------------------------------
# Problem 13: Compute Manhattan distance between two points
#   Input:  point1=(1,2), point2=(4,6)
#   Output: 7
# ---------------------------------------------------------------------------
def problem_13():
    pass


# ---------------------------------------------------------------------------
# Problem 14: Compute cosine similarity between two vectors
#   Input:  a=[1,0,1], b=[1,1,0]
#   Output: 0.5
# ---------------------------------------------------------------------------
def problem_14():
    pass


# ---------------------------------------------------------------------------
# Problem 15: Perform chi-square test on categorical data
#   Input:  observed=[30, 10, 20], expected=[20, 20, 20]
#   Output: chi2 statistic and p-value
# ---------------------------------------------------------------------------
def problem_15():
    pass


# ---------------------------------------------------------------------------
# Problem 16: Compute the determinant of a matrix
#   Input:  [[1,2],[3,4]]
#   Output: -2.0
# ---------------------------------------------------------------------------
def problem_16():
    pass


# ---------------------------------------------------------------------------
# Problem 17: Solve a system of linear equations
#   Input:  2x + y = 5, x + 3y = 10
#   Output: x=1.0, y=3.0
# ---------------------------------------------------------------------------
def problem_17():
    pass


# ---------------------------------------------------------------------------
# Problem 18: Compute eigenvalues of a matrix
#   Input:  [[2, 0], [0, 3]]
#   Output: [2, 3]
# ---------------------------------------------------------------------------
def problem_18():
    pass


# ---------------------------------------------------------------------------
# Problem 19: Perform ANOVA on three groups
#   Input:  group1=[5,6,7], group2=[8,9,10], group3=[1,2,3]
#   Output: F-statistic > 0
# ---------------------------------------------------------------------------
def problem_19():
    pass


# ---------------------------------------------------------------------------
# Problem 20: Compute the inverse of a matrix
#   Input:  [[1,2],[3,4]]
#   Output: [[-2, 1], [1.5, -0.5]]
# ---------------------------------------------------------------------------
def problem_20():
    pass


# ---------------------------------------------------------------------------
# Problem 21: Fit a curve to data using curve_fit
#   Input:  y = 2*x + 1 with noise, x=[1,2,3,4,5]
#   Output: slope ~ 2.0, intercept ~ 1.0
# ---------------------------------------------------------------------------
def problem_21():
    pass


# ---------------------------------------------------------------------------
# Problem 22: Compute the integral of a function using quad
#   Input:  integrate x^2 from 0 to 3
#   Output: 9.0
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
