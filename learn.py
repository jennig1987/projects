import pandas as pd
import numpy as np

# Creating a hypothetical sales dataset
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-10'),
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C'],
    'Sales': [100, 150, 120, 80, 200, 110, 90, 130, 160, 75],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'West', 'North', 'East', 'South']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)