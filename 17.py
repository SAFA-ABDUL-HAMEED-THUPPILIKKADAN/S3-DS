# write a python program to predict diabetes using knn classification
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
import numpy as np


diabetes = load_diabetes()

# print(diabetes.data.shape)
# print(diabetes.target.shape)
# print(len(diabetes.feature_names))
# print(diabetes.feature_names)
# print(diabetes.target)
# print(diabetes.data[0])

X = diabetes.data
Y = diabetes.target
classifier = neighbors.KNeighborsRegressor(n_neighbors=5)
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
r2 = r2_score(y_test, y_pred)
# print("R² Score:", r2)
# accuracy = accuracy_score(y_test, y_pred)*100
print(y_test)
print(y_pred)
# print(accuracy)


user_input = np.array([[
    0.03807591,   # age
    0.05068012,   # sex
    0.06169621,   # bmi
    0.02187235,   # bp
    -0.0442235,   # s1
    -0.03482076,  # s2
    -0.04340085,  # s3
    -0.00259226,  # s4
    0.01990842,   # s5
    -0.01764613   # s6
]])

prediction = classifier.predict(user_input)
# print("Predicted disease progression:", prediction[0])
