import pandas as pd
import re

# Loading in Dataset
df = pd.read_csv('data/medicalmalpractice.csv')

# Making Column Names Lowercase
df.columns = map(str.lower, df.columns)

# Removing Space in Column Name
df.columns = df.columns.map(lambda x: x.strip().replace(' ', '_'))

# Dropping Missing Values
df = df.dropna

# Save Cleaned CSV File
df.to_csv('clean_medicalmalpractice.csv', index=False)