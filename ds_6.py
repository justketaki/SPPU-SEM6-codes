import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Step 1: Importing the dataset
dataset = pd.read_csv('https://raw.githubusercontent.com/mk-gurucharan/Classification/master/IrisDataset.csv')

# Step 2: Describing and exploring the dataset
print(dataset.describe())
print(dataset.head())
print(dataset.shape)

# Step 3: Preparing features (X) and target (y)
X = dataset.iloc[:, :-1].values  # Features (sepal_length, sepal_width, petal_length, petal_width)
y = dataset['species'].values  # Target (species)

# Step 4: Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Step 6: Fitting Naive Bayes to the training set
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Step 7: Predicting the test set results
y_pred = classifier.predict(X_test)

# Step 8: Computing the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Step 9: Calculating Accuracy, Error Rate, Precision, Recall
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred, average='macro', labels=np.unique(y))
recall = recall_score(y_test, y_pred, average='macro', labels=np.unique(y))
f1 = f1_score(y_test, y_pred, average='macro', labels=np.unique(y))

# Step 10: Displaying the metrics
print(f"Accuracy: {accuracy}")
print(f"Error Rate: {error_rate}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Optional: Plotting the confusion matrix
plt.figure(figsize=(6, 4))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(len(np.unique(y)))
plt.xticks(tick_marks, np.unique(y))
plt.yticks(tick_marks, np.unique(y))
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
