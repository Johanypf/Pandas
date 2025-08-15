import pandas as pd
import numpy as np

s= pd.Series([1,3,5,np.nan,6,8])
print(s)


dates = pd.date_range("20250101",periods=6)
print(dates)

df = pd.DataFrame(np.random.randint(2,10, size=[6,4]), index=dates, columns=list("ABCD"))
print(df)
print(df.dtypes)

print(df.head(2))
print(df.tail(2))

print(df.index)
print(df.columns)

print(df.describe())

print(df["A"])
print(df[0:2])

print(df.loc["2025-01-01":"2025-01-04", ["A", "B"]])

print(df.iloc[3])
print(df.iloc[3:5, 0:2])

print(df[df > 3])