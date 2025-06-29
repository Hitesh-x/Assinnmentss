
# Assignment
# Question 1

import pandas as pd

date_s = ['2025-01-01', '2025-02-15', '2025-03-30']
date_series = pd.to_datetime(pd.Series(date_s))

print("This is TS\n")
print(date_series)

# =============================================================>>
# Question 2

# import pandas as pd
# df1 = pd.DataFrame({
#     'Name': ['a', 'b', 'c', 'd'],
#     'Subject': ['sub1', 'sub2', 'sub3', 'sub4'],
#     'marks': [23, 45, 56, 78],
#     'id': [1, 2, 3, 4]
# })
#
# df2 = pd.DataFrame({
#     'Name': ['e', 'f', 'g', 'h'],
#     'Subject': ['sub1', 'sub2', 'sub3', 'sub4'],
#     'marks': [32, 60, 68, 89],
#     'id': [1, 2, 3, 5]
# })
# inner = pd.merge(df1, df2, on='id', how='inner', suffixes=('_df1', '_df2'))
# print(inner)
#
# left = pd.merge(df1, df2, on='id', how='left', suffixes=('_df1', '_df2'))
# print(left)
#
# right = pd.merge(df1, df2, on='id', how='right', suffixes=('_df1', '_df2'))
# print(right)
#
# df1_index = df1.set_index('id')
# df2_index = df2.set_index('id')
# index_join = df1_index.join(df2_index, how='inner', lsuffix='_df1', rsuffix='_df2')
# print(index_join)

# =======================================================>>
# Question 3

# import pandas as pd
#
# df1 = pd.DataFrame({
#     'Name': ['a', 'b', 'c', 'd'],
#     'Subject': ['sub1', 'sub2', 'sub3', 'sub4'],
#     'marks': [23, 45, 56, 78],
#     'id': [1, 2, 3, 4]
# })
#
# df2 = pd.DataFrame({
#     'Name': ['e', 'f', 'g', 'h'],
#     'Subject': ['sub1', 'sub2', 'sub3', 'sub4'],
#     'marks': [32, 60, 68, 89],
#     'id': [1, 2, 3, 5]
# })
# df_combined = pd.concat([df1, df2])
# print("Concatenated DataFrame:\n", df_combined)
#
# merged_df = pd.merge(df1, df2, on='id', how='inner',
#                      suffixes=('_df1', '_df2'))
# print("\nMerged DataFrame IS:\n", merged_df)