# -*- coding: utf-8 -*-
"""Logistic regression assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ycI1pw4-TEomdGeDRoLKrl2AjZFHx0ho
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
train = pd.read_csv('Titanic_train.csv')
test = pd.read_csv('Titanic_test.csv')

# Quick look
print(train.head())
print(train.info())
print(train.describe())

# Visualizations
sns.countplot(data=train, x='Survived')
plt.title('Survival Distribution')
plt.show()

sns.histplot(data=train, x='Age', kde=True)
plt.title('Age Distribution')
plt.show()

sns.boxplot(data=train, x='Pclass', y='Age')
plt.title('Age vs Passenger Class')
plt.show()

# Select only numerical features for correlation analysis
numerical_features = train.select_dtypes(include=['number'])

# Calculate the correlation matrix for numerical features
correlation_matrix = numerical_features.corr()

# Generate the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
        'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
train = pd.read_csv('Titanic_train.csv', names=cols)

test = pd.read_csv('Titanic_test.csv')

train = pd.read_csv('Titanic_train.csv', header=0)

import pandas as pd

train = pd.read_csv('Titanic_train.csv')

# Check column names
print(train.columns.tolist())

# Remove any extra spaces in column names
train.columns = train.columns.str.strip()

# Now you can fillna safely
train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)

# Handling missing values
train['Age'].fillna(train['Age'].median(), inplace=True)
train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' due to many missing values
train.drop('Cabin', axis=1, inplace=True)

# Encoding categorical variables
train = pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True)

# Drop unnecessary columns
train.drop(['Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)

# Final features
X = train.drop('Survived', axis=1)
y = train['Survived']

#Model building
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#Model Evaluation
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve

y_pred = model.predict(X_val)
y_prob = model.predict_proba(X_val)[:,1]

print("Accuracy:", accuracy_score(y_val, y_pred))
print("Precision:", precision_score(y_val, y_pred))
print("Recall:", recall_score(y_val, y_pred))
print("F1 Score:", f1_score(y_val, y_pred))
print("ROC AUC Score:", roc_auc_score(y_val, y_prob))

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_val, y_prob)
plt.plot(fpr, tpr, label="ROC curve")
plt.plot([0,1], [0,1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

#Interpretation
# Coefficients interpretation
coef_df = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_[0]})
print(coef_df.sort_values(by='Coefficient', ascending=False))

