"""
Chapter 02: Pandas Tutorial
=============================

Notes
-----
- Pandas provides DataFrame and Series for data manipulation and analysis.
- Install: pip install pandas
- Import: import pandas as pd
- Create DataFrame: pd.DataFrame({"col1": [1,2], "col2": [3,4]}).
- Read CSV: pd.read_csv("data.csv").
- Key operations: df.head(), df.describe(), df["col"], df[df["col"] > 5].
- Missing values: df.isna(), df.fillna(0), df.dropna().

Run:  python3 chapters/04_libraries/02_pandas_tutorial.py
"""

# pip install pandas

# ---------------------------------------------------------------------------
# Problem 1: Create a DataFrame from a dictionary and access a column
#   Input:  pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})["age"]
#   Output: [25, 30]
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Filter rows based on a condition
#   Input:  df = pd.DataFrame({"product": ["A","B","C"], "price": [10, 25, 15]})
#           filter price > 12
#   Output: ["B", "C"]
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Add a new column computed from existing columns
#   Input:  df = pd.DataFrame({"math": [80, 90], "science": [70, 95]})
#           add "average" column
#   Output: [75.0, 92.5]
# ---------------------------------------------------------------------------
def problem_3():
    pass


# ---------------------------------------------------------------------------
# Problem 4: Get the shape of a DataFrame
#   Input:  df = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]})
#   Output: (3, 2)
# ---------------------------------------------------------------------------
def problem_4():
    pass


# ---------------------------------------------------------------------------
# Problem 5: Get the column names of a DataFrame
#   Input:  df = pd.DataFrame({"x": [1], "y": [2], "z": [3]})
#   Output: ["x", "y", "z"]
# ---------------------------------------------------------------------------
def problem_5():
    pass


# ---------------------------------------------------------------------------
# Problem 6: Get the first N rows using head()
#   Input:  df with 5 rows, df.head(3)
#   Output: first 3 rows
# ---------------------------------------------------------------------------
def problem_6():
    pass


# ---------------------------------------------------------------------------
# Problem 7: Get the last N rows using tail()
#   Input:  df with 5 rows, df.tail(2)
#   Output: last 2 rows
# ---------------------------------------------------------------------------
def problem_7():
    pass


# ---------------------------------------------------------------------------
# Problem 8: Compute basic statistics with describe()
#   Input:  df = pd.DataFrame({"values": [10, 20, 30, 40, 50]})
#           df["values"].mean()
#   Output: 30.0
# ---------------------------------------------------------------------------
def problem_8():
    pass


# ---------------------------------------------------------------------------
# Problem 9: Sort a DataFrame by a column
#   Input:  df = pd.DataFrame({"name": ["C","A","B"], "score": [30, 10, 20]})
#           sort by "score" ascending
#   Output: ["A", "B", "C"]
# ---------------------------------------------------------------------------
def problem_9():
    pass


# ---------------------------------------------------------------------------
# Problem 10: Rename columns of a DataFrame
#   Input:  df = pd.DataFrame({"a": [1], "b": [2]})
#           rename columns to {"a": "x", "b": "y"}
#   Output: ["x", "y"]
# ---------------------------------------------------------------------------
def problem_10():
    pass


# ---------------------------------------------------------------------------
# Problem 11: Drop a column from a DataFrame
#   Input:  df = pd.DataFrame({"a": [1,2], "b": [3,4], "c": [5,6]})
#           drop column "b"
#   Output: columns are ["a", "c"]
# ---------------------------------------------------------------------------
def problem_11():
    pass


# ---------------------------------------------------------------------------
# Problem 12: Fill missing values in a DataFrame
#   Input:  df = pd.DataFrame({"a": [1, None, 3], "b": [None, 2, 3]})
#           df.fillna(0)
#   Output: [[1, 0], [0, 2], [3, 3]]
# ---------------------------------------------------------------------------
def problem_12():
    pass


# ---------------------------------------------------------------------------
# Problem 13: Drop rows with missing values
#   Input:  df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, 6]})
#           df.dropna()
#   Output: 2 rows remaining
# ---------------------------------------------------------------------------
def problem_13():
    pass


# ---------------------------------------------------------------------------
# Problem 14: Count occurrences of each value in a column
#   Input:  df = pd.DataFrame({"color": ["red","blue","red","green","blue","red"]})
#           df["color"].value_counts()
#   Output: red: 3, blue: 2, green: 1
# ---------------------------------------------------------------------------
def problem_14():
    pass


# ---------------------------------------------------------------------------
# Problem 15: Get unique values of a column
#   Input:  df = pd.DataFrame({"a": [1, 2, 2, 3, 3, 3]})
#           df["a"].unique()
#   Output: [1, 2, 3]
# ---------------------------------------------------------------------------
def problem_15():
    pass


# ---------------------------------------------------------------------------
# Problem 16: Apply a function to a column
#   Input:  df = pd.DataFrame({"temp_c": [0, 20, 100]})
#           convert to Fahrenheit: temp_c * 9/5 + 32
#   Output: [32.0, 68.0, 212.0]
# ---------------------------------------------------------------------------
def problem_16():
    pass


# ---------------------------------------------------------------------------
# Problem 17: Group by a column and compute mean
#   Input:  df = pd.DataFrame({"dept": ["A","A","B","B"], "salary": [50,60,70,80]})
#           group by "dept", mean salary
#   Output: A: 55.0, B: 75.0
# ---------------------------------------------------------------------------
def problem_17():
    pass


# ---------------------------------------------------------------------------
# Problem 18: Merge two DataFrames on a common column
#   Input:  df1 = pd.DataFrame({"id": [1,2], "name": ["A","B"]})
#           df2 = pd.DataFrame({"id": [2,3], "score": [80, 90]})
#           merge on "id"
#   Output: 1 row (id=2, name=B, score=80)
# ---------------------------------------------------------------------------
def problem_18():
    pass


# ---------------------------------------------------------------------------
# Problem 19: Create a DataFrame from a list of lists
#   Input:  [["Alice", 85], ["Bob", 92]], columns=["name", "score"]
#   Output: DataFrame with 2 rows and 2 columns
# ---------------------------------------------------------------------------
def problem_19():
    pass


# ---------------------------------------------------------------------------
# Problem 20: Iterate over rows of a DataFrame
#   Input:  df = pd.DataFrame({"x": [10, 20], "y": [30, 40]})
#           sum of x + y for each row
#   Output: [40, 60]
# ---------------------------------------------------------------------------
def problem_20():
    pass


# ---------------------------------------------------------------------------
# Problem 21: Filter rows using multiple conditions (AND)
#   Input:  df = pd.DataFrame({"a": [1,2,3,4], "b": [10,20,30,40]})
#           filter a > 1 and b < 40
#   Output: rows with a=2,b=20 and a=3,b=30
# ---------------------------------------------------------------------------
def problem_21():
    pass


# ---------------------------------------------------------------------------
# Problem 22: Filter rows using multiple conditions (OR)
#   Input:  df = pd.DataFrame({"a": [1,2,3,4], "b": [10,20,30,40]})
#           filter a == 1 or b == 40
#   Output: rows with (1,10) and (4,40)
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
