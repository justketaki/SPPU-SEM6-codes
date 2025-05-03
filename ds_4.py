# Step 1: Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load the dataset
data = pd.read_csv('boston_housing.csv')

# Step 3: Check the column names of the dataset
print("Column names:", data.columns)

# Step 4: Explore the dataset (viewing first few rows and description)
print(data.head())
print(data.describe())

# Step 5: Check for missing values
print(data.isnull().sum())

# Step 6: Split the data into features and target
# The correct target column name is 'price', not 'PRICE'
X = data.drop('price', axis=1)  # Features (all columns except the target 'price')
y = data['price']  # Target (the house prices 'price')

# Step 7: Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 9: Make predictions on the test data
y_pred = model.predict(X_test)

# Step 10: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Output evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
print(f'R^2 Score: {r2}')

# Step 11: Visualize the results (optional)
plt.scatter(y_test, y_pred)
plt.xlabel('True Prices')
plt.ylabel('Predicted Prices')
plt.title('True vs Predicted House Prices')
plt.show()
