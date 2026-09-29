import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"], "Marks": [79, 92, 78]}

df = pd.DataFrame(data)

# i) Create DataFrame
print(df)

# ii) Display entire dataset


# iii) Display record at index 0
print("0 location")
print(df.loc[0])

# iv) Display students who scored more than 80
print("more than 80")
print(df[df["Marks"] > 80])
