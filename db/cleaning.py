import pandas as pd
import re

# Loading in Dataset
df = pd.read_csv('data/behavior_health.csv')

# Making Column Names Lowercase
df.columns = map(str.lower, df.columns)

# Dropping a Column
column_to_remove = 'dataquality'
df = df.drop(column_to_remove, axis=1)

# Dropping Unknown Values
servicecount_value_counts = df['servicecount'].value_counts()
rate_value_counts = df['rateper1000beneficiaries'].value_counts()

df = df[df['servicecount'] != 'DQ']
df = df[df['servicecount'] != 'DS']
df = df[df['rateper1000beneficiaries'] != 'DQ']

# Dropping Missing Values
df = df.dropna