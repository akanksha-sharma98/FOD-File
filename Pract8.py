#  Perform Statistics and Data Visualization in python.

import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
data = np.random.normal(0, 1, 1000)

# Perform basic statistics
mean_value = np.mean(data)
std_dev = np.std(data)
median_value = np.median(data)

# Data Visualization
# Histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=False)
plt.title('Boxplot of Random Data')
plt.xlabel('Value')
plt.show()

# Scatter plot with a trendline
x = np.random.normal(0, 1, 1000)
y = 2 * x + np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5)
plt.plot(x, 2 * x, color='red', linewidth=2, label='Trendline')
plt.title('Scatter Plot with Trendline')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Print the calculated statistics
print("Mean:", mean_value)
print("Standard Deviation:", std_dev)
print("Median:", median_value)
