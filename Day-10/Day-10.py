
# ASSIGNMENT

# Question 1

import numpy as np

arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])

print("Original Array:")
print(arr)

arr[np.isnan(arr)] = 0

print("\nArray replacing NaN:")
print(arr)

sub_array = arr[:, :3]
transposed = sub_array.T

print("\nTransposed \n:")
print(transposed)


# ===========================================================>>
# Question 2

# import numpy as np
#
# arr3d = np.random.randint(1, 10, (2, 3, 4))
#
# print("Original Arrayss:", arr3d.shape)
# print("Original Array:\n", arr3d)
#
# moved = np.moveaxis(arr3d, 0, -1)
#
# print("\nAfter Axis\n:")
# print("New Shape:", moved.shape)
# print("Moved Array:\n", moved)

# =============================================================>>
# Question 3

# import numpy as np
# import pandas as pd
#
# data = [
#     [1, 2, np.nan],
#     [4, np.nan, 6]
# ]
#
# df = pd.DataFrame(data)
# df = df.apply(lambda col: col.fillna(col.mean()), axis=0)
#
# arr = df.to_numpy()
#
# print("Array after REPLACE\n:")
# print(arr)

# ================================================================>>

# Question 4


# import numpy as np
#
# arr = np.array([
#     [5, -3, 8],
#     [-7, 2, -1]
# ])
#
# arr = np.where(arr < 0, 0, arr)
#
# print("Array after Update\n:")
# print(arr)

# ===================================================================>>
# Question 5

# import numpy as np
# a = np.array([[1, np.nan, 3], [np.nan, 5, 6]])
# print(np.isnan(a).sum())


# =====================================================================>>
# Question 6

# import numpy as np
#
# arr1 = np.array([3, 4])
# arr2 = np.array([1, 0])
#
# avg = (arr1 + arr2) / 2
#
# print("Average:\n")
# print(avg)


# ========================================================================>>
# Question 7

# import numpy as np
#
# arr1 = np.array([[3, 4], [5, 6]])
# arr2 = np.array([[1, 0], [7, 2]])
#
# avg = (arr1 + arr2) / 2
#
# print("Average:\n", avg)
# print("Mean:", np.mean(avg))
# print("Median:", np.median(avg))

# ============================================================================>>
# Questino 8

# import numpy as np
#
# A = np.array([[1, -2, 3],
#               [-1, 3, -1],
#               [2, -5, 5]])
#
# B = np.array([9, -6, 17])
#
# X1 = np.linalg.solve(A, B)
# A_inv = np.linalg.inv(A)
# X2 = np.dot(A_inv, B)
#
# print(X1)
# print(X2)

# ===============================================================================>>
# Question 9

# import matplotlib.pyplot as plt
#
# students = ['A', 'B', 'C', 'D', 'E']
# sem1 = [65, 70, 75, 80, 85]
# sem2 = [68, 72, 78, 82, 88]
#
# plt.plot(students, sem1, label='Sem 1', marker='o')
# plt.plot(students, sem2, label='Sem 2', marker='s')
# plt.title('Result Comparison')
# plt.xlabel('Students')
# plt.ylabel('Marks')
# plt.legend()
# plt.grid(True)
# plt.show()
