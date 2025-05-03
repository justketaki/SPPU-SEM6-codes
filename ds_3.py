# Title of Assignment: Descriptive Statistics - Measures of Central Tendency and Variability

# Step 0: Import Required Libraries
import pandas as pd
import numpy as np

# Step 1: Load the Dataset
df = pd.read_csv("loan.csv.csv")
print("First 5 rows of the dataset:\n", df.head())

# Step 2: Display Dataset Info
print("\nDataset Info:")
df.info()

# Step 3: Handle Missing Values
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Fill missing numeric values with mean and categorical values with mode
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(), inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

print("\nMissing values after cleaning:\n", df.isnull().sum())

# Step 4: Summary statistics of LoanAmount grouped by Loan_Status
grouped = df.groupby('Loan_Status')['LoanAmount'].agg(['mean', 'median', 'min', 'max', 'std'])
print("\nSummary statistics of 'LoanAmount' grouped by 'Loan_Status':\n", grouped)

# Step 5: Create a list that contains loan amounts for each Loan_Status group
print("\nList of LoanAmount values by Loan_Status:")
value_lists = {}
for status in df['Loan_Status'].unique():
    value_lists[status] = df[df['Loan_Status'] == status]['LoanAmount'].tolist()
    print(f"{status}: {value_lists[status][:5]}... (total {len(value_lists[status])} values)")

# Optional: Save grouped summary to CSV
grouped.to_csv("loan_summary_by_Loan_Status.csv")
print("\nGrouped summary saved as 'loan_summary_by_Loan_Status.csv'")

# Title: Statistical Summary for Iris Dataset by Species

# Step 1: Import Required Libraries
import pandas as pd

# Step 2: Load the Dataset
df = pd.read_csv("Iris.csv")

# Step 3: Display basic info
print("First 5 rows of the dataset:\n", df.head())
print("\nUnique Species in Dataset:", df['Species'].unique())

# Step 4: Group by Species and describe each group
species_list = df['Species'].unique()

for species in species_list:
    print(f"\nStatistical details for {species}:")
    print(df[df['Species'] == species].describe())

# Optional: Save descriptive stats for each species to separate CSVs
for species in species_list:
    stats = df[df['Species'] == species].describe()
    filename = f"{species.replace('-', '_')}_stats.csv"
    stats.to_csv(filename)
    print(f"Saved statistical summary for {species} to '{filename}'")
