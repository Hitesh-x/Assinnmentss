
# ASSIGNMENT

# Question 1

# import numpy as np
#
# a1 = np.array([1, 2])
# a2 = np.array([[3, 4], [5, 6]])
# a1_reshaped = a1.reshape(1, 2)
# combined = np.vstack((a2, a1_reshaped))
#
# print("Combined Array:\n", combined)

# =====================================================>>

# Question 2

# import numpy as np
#
# a2 = np.array([[3, 4], [5, 6]])
# flat = a2.flatten()
#
# print("Flattened Array:", flat)

# ========================================================>>

# Question 3

# import numpy as np
#
# a1 = np.array([1, 2, 3, 4])
# reversed_a1 = a1[::-1]
#
# print("Reversed Array:", reversed_a1)

# ========================================================>>

# Question 4

import numpy as np

a = np.array([[10, 20], [5, 15]])
print("Max:", a.max(), "Min:", a.min(), "Shape:", a.shape)
print("Row:", a[0], "Col:", a[:,1], "Elem:", a[1,1])
print("Sum:", sum(i for r in a for i in r))

b = np.array([[1, 2], [3, 4]])
c = np.array([[5, 6], [7, 8]])
print("Add:\n", b+c, "\nSub:\n", b-c, "\nMul:\n", b*c, "\nDiv:\n", b/c)
