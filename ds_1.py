# Title of the Assignment: Data Wrangling I

# Step 0: Import Required Python Libraries
import pandas as pd
import numpy as np

# Step 1: Locate open source data
# (We are using data.csv that has been uploaded for this assignment)
# Example source if needed: https://www.kaggle.com/datasets

# Step 2: Provide a clear description of the data and its source
# This step is to be described in the report, not in code.
# We'll explore the dataset below.

# Step 3: Load the Dataset into the pandas data frame
df = pd.read_csv("data.csv")
print("First 5 rows of the dataset:\n", df.head())

# Step 4: Data Preprocessing

# Check for missing values
print("\nMissing values in each column:\n", df.isnull().sum())

# Get initial statistics
print("\nDescriptive statistics of the dataset:\n", df.describe(include='all'))

# Check variable descriptions and data types
print("\nData Types of each column:\n", df.dtypes)

# Check dimensions of the data frame
print("\nShape of the dataset:", df.shape)

# Step 5: Data Formatting and Normalization

# Convert object types to category where appropriate
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype('category')

# If required, convert float columns to integers (example shown, can modify as per column names)
# df['column_name'] = df['column_name'].astype('int64')

# Print updated data types
print("\nUpdated Data Types:\n", df.dtypes)

# Step 6: Turn categorical variables into quantitative variables

# One-hot encoding of categorical variables
df_encoded = pd.get_dummies(df, drop_first=True)

# Display the new DataFrame with encoded variables
print("\nFirst 5 rows of the encoded DataFrame:\n", df_encoded.head())

# Optional: Save the cleaned and encoded dataset
df_encoded.to_csv("cleaned_data.csv", index=False)
print("\nCleaned and encoded dataset saved as 'cleaned_data.csv'")
