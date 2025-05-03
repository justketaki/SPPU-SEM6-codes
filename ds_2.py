# Title of the Assignment: Data Wrangling II

# Step 0: Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.preprocessing import PowerTransformer

# Step 1: Load the Academic Performance Dataset
df = pd.read_csv("acdemic_data.csv")
print("First 5 rows of the dataset:\n", df.head())

# Step 2: Scan for Missing Values and Inconsistencies
print("\nMissing values in each column:\n", df.isnull().sum())

# Fill missing values - example strategies:
# Numeric: fill with mean; Categorical: fill with mode
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

print("\nMissing values after imputation:\n", df.isnull().sum())

# Step 3: Scan Numeric Variables for Outliers
numeric_cols = df.select_dtypes(include=[np.number]).columns

print("\nZ-score based outlier detection:")
for col in numeric_cols:
    z_scores = zscore(df[col])
    outliers = np.where(np.abs(z_scores) > 3)[0]
    print(f"{col}: {len(outliers)} outliers")

# Option: Remove outliers (based on Z-score > 3)
for col in numeric_cols:
    df = df[(np.abs(zscore(df[col])) < 3)]

print("\nShape after removing outliers:", df.shape)

# Step 4: Data Transformation (e.g., skewness correction for a variable)
# Select a skewed variable (example: 'marks')
# Check skewness before transformation
if 'marks' in df.columns:
    print("\nSkewness of 'marks' before transformation:", df['marks'].skew())

    # Apply PowerTransformer (Yeo-Johnson handles both positive/negative values)
    pt = PowerTransformer(method='yeo-johnson')
    df['marks_transformed'] = pt.fit_transform(df[['marks']])

    # Check skewness after transformation
    print("Skewness of 'marks_transformed' after transformation:", pd.Series(df['marks_transformed']).skew())

    # Optional: Visualize distribution before and after
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df['marks'], kde=True)
    plt.title('Original Marks Distribution')
    
    plt.subplot(1, 2, 2)
    sns.histplot(df['marks_transformed'], kde=True)
    plt.title('Transformed Marks Distribution')
    plt.show()
else:
    print("\nColumn 'marks' not found. Replace with a numeric column from your dataset for transformation.")

# Optional: Save cleaned and transformed dataset
df.to_csv("academic_cleaned.csv", index=False)
print("\nCleaned and transformed dataset saved as 'academic_cleaned.csv'")
