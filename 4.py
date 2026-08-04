from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np


iris = load_iris()
X = iris.data
y = iris.target



X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)
y_prediction = model.predict(X_test)
print(y_prediction)
print(y_test)

print(accuracy_score(y_test, y_prediction))
print(confusion_matrix(y_test, y_prediction))
print(classification_report(y_test,y_prediction))


sample = np.array([[8.1,2.5,3.4,8.2]])
prediction = model.predict(sample)
print(iris.target_names[prediction])

print(iris.target_names)

