# Create a synthetic dataset (.csv/.xlsx) to work upon and design a Python program to read and print that data.

import pandas as pd
import numpy as np

# Create a synthetic dataset
data = {
    'Name': ['Akanksha', 'Jeet', 'Charlie', 'Karan', 'Roshni'],
    'Age': np.random.randint(20, 40, size=5),
    'Salary': np.random.randint(30000, 80000, size=5),
    'City': ['Delhi', 'Noida', 'Faridabad', 'Mumbai', 'Pataila']
}

df = pd.DataFrame(data)

     # Save the dataset to CSV and Excel files
df.to_csv('synthetic_dataset.csv', index=False)
df.to_excel('synthetic_dataset.xlsx', index=False)

print("Synthetic dataset created and saved to synthetic_dataset.csv and synthetic_dataset.xlsx")

df_csv = pd.read_csv('synthetic_dataset.csv')
# Read the dataset from CSV

df_excel = pd.read_excel('synthetic_dataset.xlsx')
# Read the dataset from Excel

print("\nDataset from CSV:\n", df_csv)
print("\nDataset from Excel:\n", df_excel)
     # Print the datasets...
     