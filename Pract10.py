# Design a Python program using NumPy library functions.

import numpy as np

# Create a NumPy array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print the original array
print("Original array:")
print(data)

# Perform some basic NumPy operations
mean_value = np.mean(data)
sum_value = np.sum(data)
max_value = np.max(data)
min_value = np.min(data)
transpose_data = np.transpose(data)

# Print the results
print("\nMean:", mean_value)
print("Sum:", sum_value)
print("Maximum:", max_value)
print("Minimum:", min_value)
print("\nTransposed array:")
print(transpose_data)            # print the transposed array

