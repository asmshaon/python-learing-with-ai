from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"

# mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}

# myvar = pd.DataFrame(mydataset)

# a = [1, 7, 2]

# myvar = pd.Series(a, index=["x", "y", "z", "u"])

# # print(myvar["x"])


df = pd.read_csv(DATA_DIR / "sales.csv", parse_dates=["order_date"])
print(df.head())
print(df.describe())

# print(df.head())
