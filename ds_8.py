import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
dataset = sns.load_dataset('titanic')

# Display first few rows of the dataset
print(dataset.head())

# Plotting the histogram of 'fare' using histplot (updated method)
sns.histplot(dataset['fare'], kde=True, bins=20, color='blue')
plt.title('Distribution of Ticket Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Another histogram with no KDE (kernel density estimate)
sns.histplot(dataset['fare'], kde=False, bins=20, color='green')
plt.title('Histogram of Ticket Fare (No KDE)')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Jointplot between 'age' and 'fare'
sns.jointplot(x='age', y='fare', data=dataset)
plt.show()

# Jointplot with hexbin style for better visualization of dense areas
sns.jointplot(x='age', y='fare', data=dataset, kind='hex')
plt.show()

# Pairplot to visualize relationships between numeric features, colored by 'sex'
dataset_cleaned = dataset.dropna()  # Remove rows with missing values
sns.pairplot(dataset_cleaned, hue='sex')
plt.show()

# Rugplot to visualize individual points of 'fare' along the x-axis
sns.rugplot(dataset['fare'])
plt.title('Rugplot of Ticket Fare')
plt.xlabel('Fare')
plt.show()

# Final updated histogram with KDE and more details
plt.figure(figsize=(10, 6))
sns.histplot(dataset['fare'], kde=True, bins=30, color='blue')
plt.title('Distribution of Ticket Fare with KDE')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()
