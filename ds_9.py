# ===========================
# Import Libraries and Load Data
# ===========================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset

# Load Titanic dataset
data = pd.read_csv("titanic_Dataset.csv")

# Load Tips dataset
tips = load_dataset("tips")

# Display column names to verify
print("Titanic Dataset Columns:\n", data.columns)

# ===========================
# Univariate Analysis
# ===========================

# --- Categorical Data ---

# 1. Countplot of Survived
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=data)
plt.title("Count of Survival")
plt.show()

# 2. Pie Chart of Sex
plt.figure(figsize=(6, 6))
data['Sex'].value_counts().plot(kind="pie", autopct="%.2f%%", startangle=90, shadow=True)
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# --- Numerical Data ---

# 3. Histogram of Age
plt.figure(figsize=(6, 4))
plt.hist(data['Age'].dropna(), bins=5, color='skyblue')
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 4. Distplot of Age with KDE
plt.figure(figsize=(6, 4))
sns.histplot(data['Age'].dropna(), kde=True, color='purple')
plt.title("Distribution of Age with KDE")
plt.xlabel("Age")
plt.show()

# ===========================
# Box Plot (as per Aim)
# ===========================

# 5. Boxplot: Age by Gender and Survived
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sex', y='Age', hue='Survived', data=data)
plt.title("Box Plot of Age by Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.show()

# ===========================
# Bivariate and Multivariate Analysis
# ===========================

# 6. Bar Plot: Pclass vs Age
plt.figure(figsize=(6, 4))
sns.barplot(x='Pclass', y='Age', data=data)
plt.title("Average Age per Pclass")
plt.xlabel("Pclass")
plt.ylabel("Age")
plt.show()

# 7. Bar Plot with Hue: Pclass vs Fare by Sex
plt.figure(figsize=(6, 4))
sns.barplot(x='Pclass', y='Fare', hue='Sex', data=data)
plt.title("Fare by Pclass and Gender")
plt.xlabel("Pclass")
plt.ylabel("Fare")
plt.show()

# 8. Distplot: Age Distribution by Survival
plt.figure(figsize=(8, 5))
sns.histplot(data[data['Survived'] == 0]['Age'].dropna(), kde=True, color="blue", label="Not Survived")
sns.histplot(data[data['Survived'] == 1]['Age'].dropna(), kde=True, color="orange", label="Survived")
plt.title("Age Distribution: Survived vs Not Survived")
plt.xlabel("Age")
plt.legend()
plt.show()

# ===========================
# Categorical vs Categorical
# ===========================

# 9. Heatmap: Pclass vs Survived
cross_tab = pd.crosstab(data['Pclass'], data['Survived'])
plt.figure(figsize=(6, 4))
sns.heatmap(cross_tab, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Heatmap of Pclass vs Survival")
plt.xlabel("Survived")
plt.ylabel("Pclass")
plt.show()

# 10. Clustermap: Parch vs Survived
sns.clustermap(pd.crosstab(data['Parch'], data['Survived']), cmap="coolwarm", annot=True)
plt.title("Clustermap of Parch vs Survival")
plt.show()

# ===========================
# Extra: Scatter Plot from Tips Dataset
# ===========================

# 11. Scatter Plot: Total Bill vs Tip
plt.figure(figsize=(6, 4))
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# 12. Multivariate Scatter: Total Bill vs Tip by Gender
plt.figure(figsize=(6, 4))
sns.scatterplot(x='total_bill', y='tip', hue='sex', data=tips)
plt.title("Total Bill vs Tip by Gender")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# 13. Multivariate Scatter: Total Bill vs Tip by Gender and Smoker
plt.figure(figsize=(6, 4))
sns.scatterplot(x='total_bill', y='tip', hue='sex', style='smoker', data=tips)
plt.title("Total Bill vs Tip by Gender and Smoker Status")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()
