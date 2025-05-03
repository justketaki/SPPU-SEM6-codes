# =============================
# 1. Import Required Libraries
# =============================
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =============================
# 2. Load the Iris Dataset
# =============================
df = pd.read_csv("Iris.csv")
print(df.head())

# =============================
# 3. Dataset Info
# =============================
print("\n--- Dataset Info ---")
df.info()

# =============================
# 4. Feature Types
# =============================
print("\n--- Feature Types ---")
print(df.dtypes)

# =============================
# 5. Unique Classes in Target
# =============================
print("\n--- Unique Classes in 'Species' ---")
print(np.unique(df["Species"]))

# =============================
# 6. Descriptive Statistics
# =============================
print("\n--- Summary Statistics ---")
print(df.describe())

# =============================
# 7. Histograms for Feature Distributions
# =============================
plt.figure(figsize=(16, 8))

plt.subplot(2, 2, 1)
plt.hist(df["SepalLengthCm"], color='skyblue', edgecolor='black')
plt.title("Histogram of Sepal Length")

plt.subplot(2, 2, 2)
plt.hist(df["SepalWidthCm"], color='lightgreen', edgecolor='black')
plt.title("Histogram of Sepal Width")

plt.subplot(2, 2, 3)
plt.hist(df["PetalLengthCm"], color='salmon', edgecolor='black')
plt.title("Histogram of Petal Length")

plt.subplot(2, 2, 4)
plt.hist(df["PetalWidthCm"], color='plum', edgecolor='black')
plt.title("Histogram of Petal Width")

plt.tight_layout()
plt.show()

# =============================
# 8. Boxplots for Outlier Detection
# =============================
data_to_plot = [
    df["SepalLengthCm"],
    df["SepalWidthCm"],
    df["PetalLengthCm"],
    df["PetalWidthCm"]
]

# Create boxplot using matplotlib
sns.set_style("whitegrid")
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ax.boxplot(data_to_plot, patch_artist=True, labels=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"])
ax.set_title("Boxplot of Iris Dataset Features")
plt.ylabel("Centimeters")
plt.show()

# Creating a figure instance
fig = plt.figure(1, figsize=(12,8))

# Creating an axes instance
ax = fig.add_subplot(111)

# Creating the boxplot
bp = ax.boxplot(data_to_plot);

