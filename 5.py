#implement gaussianNB using the public dataset load_breastcancer

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np


breastCancer = load_breast_cancer()
X = breastCancer.data
y = breastCancer.target



X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)
y_prediction = model.predict(X_test)
print(y_prediction)
print(y_test)

print(accuracy_score(y_test, y_prediction))
print(confusion_matrix(y_test, y_prediction))
print(classification_report(y_test,y_prediction))

sample = X_test[0].reshape(1,-1)
prediction = model.predict(sample)
print("Predicted classes", breastCancer.target_names[prediction])



print(breastCancer.target_names)





















