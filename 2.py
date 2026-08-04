import pandas as pd

data = {"name":["abc","xyz","pqr"],"age":[12,23,45],"salary":[25000,45000,56000],"role":["clerk","manager","md"]}

df = pd.DataFrame(data)

print(df)
print(df.loc[0])

