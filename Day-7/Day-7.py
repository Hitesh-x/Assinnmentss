# Assignment -7

# Question  1

import pandas as pd

data = {
    'Email': ['abc@.com', 'xyz@.com'],
    'Mobile': ['9876543210', '1234567890']
}

df = pd.DataFrame(data)
df['Emaill'] = df['Email'].str.contains('@')
df['Mobilee'] = df['Mobile'].str.len() == 10

print("Output of the Code::\n")
print(df)

# ================================================>>

# Question 2

# import pandas as pd
#
# data = {'Date': ['2025-06-25', '2023-12-31', '2024-01-01']}
# df = pd.DataFrame(data)
#
# df['Date'] = pd.to_datetime(df['Date'])
#
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day
#
# print("\nOutput of the Question::\n")
# print(df)

#=====================================================>>

# Question  3

# import pandas as pd
# import numpy as np
#
# data = {
#     'Name': ['Hitesh', 'Deepak', 'Hitesh', 'Hk', np.nan],
#     'City': ['Jaipur', 'GangaNagar', 'Jaipur', 'Siker', 'Jaipur'],
#     'Age': [25, 30, np.nan, 22, 28]
# }
# df = pd.DataFrame(data)
#
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df['Name'] = df['Name'].fillna('Kon h tu')
#
# citytotal = df['City'].value_counts()
#
# print("Cleaned Data is::\n", df)
# print("\nCount in Every City::\n", citytotal)
#
# print("\nFinished Assignment\n")