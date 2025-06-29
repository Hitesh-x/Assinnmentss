# Python Pandas ------>>
# Question 1

import pandas as pd
ds1 = {"a": 100, "b": 200, "c": 300}
s1 = pd.Series(ds1)

print("Dictionary in Series:")
print(s1)
ds2 = [10, 20, 30, 40]
s2 = pd.Series(ds2)

print(" List:")
print(s2)
print("\n In the Indexing:", s2[2])
print("Access Element is:", s1['b'])

# ======================================================>>
 # Question 2
 # DataFrames in Pandas

import pandas as pd

data1 = [[1, 'A'], [2, 'B']]
df1 = pd.DataFrame(data1, columns=['ID', 'Code'])
print("DataFrame List IS:")
print(df1)

data2 = {'Name': ['Hitesh', 'Deepak'], 'Age': [20, 21]}
df2 = pd.DataFrame(data2)
print("DataFrame IS:")
print(df2)

data3 = [['Amit', 85], ['Ravi', 90]]
df3 = pd.DataFrame(data3, columns=['Name', 'Marks'])
print("DF Lists:")
print(df3)

data4 = [('MOTU', 23), ('ASHU', 25)]
df4 = pd.DataFrame(data4, columns=['Name', 'Age'])
print("DF List of Tuples:")
print(df4)

data5 = [{'name': 'Milkha', 'score': 90}, {'name': 'Singh', 'score': 100}]
df5 = pd.DataFrame(data5)
print("DF List of Dictionaries:")
print(df5)

# =============================================================>>
# Question 3

import pandas as pd

df = pd.DataFrame({'Student': ['Hitesh', 'Meena', 'Ravi', 'Deepak'], 'Score': [88, 76, 90, 70]})
print(df)

for _, row in df.iterrows():
    print(f"{row['Student']} scored {row['Score']}")

print(df[df['Score'] > 75])
print(df.iloc[2])
print(df.loc[0:2, ['Student']])
congrats = df[df['Score'] >= 80]
print(congrats)

new = pd.DataFrame({'Student': ['Aarti'], 'Score': [85]})
df = pd.concat([df.iloc[:1], new, df.iloc[1:]]).reset_index(drop=True)
print(df)
print(df.values.tolist())
