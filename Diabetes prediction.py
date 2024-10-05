# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G0ik78qGpG1wonZHO1LC3bpeQwbLP7Fv
"""

#1.Data Loading and Preprocessing
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

url = pd.read_csv('/content/pima-data.csv')
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
print(url.head())

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#2. Model Training
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

#3. Predict Diabetes Function
def predict_diabetes(patient_data):
    patient_data = scaler.transform(np.array(patient_data).reshape(1, -1))

    prediction = model.predict(patient_data)[0]

    return "Positive" if prediction == 1 else "Negative"

#4.Predict outcome for the new patient
new_patient = [5, 120, 70, 20, 80, 25.0, 0.5, 33]
result = predict_diabetes(new_patient)
print(f"Diabetes Prediction for the patient: {result}")

#5. Model Evaluation
from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("Confusion Matrix:")
print(conf_matrix)