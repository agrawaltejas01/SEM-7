import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import data
dataset = pd.read_csv("/home/test/BE/CL-7_practice/ML/Ass_5_SVM_python/Social_Network_Ads.csv")
X = dataset.iloc[:, [2,3]].values
Y = dataset.iloc[:, 4].values

#Split in train and test
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

#Scale
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#SVM
from sklearn.svm import SVC
classifier = SVC(kernel = "linear", random_state = 0)
classifier.fit(X_train, Y_train)

#Predict
y_pred = classifier.predict(X_test)

#Confussion_Matrix and accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)
cm
accuracy = (cm[0,0] + cm[1,1]) / (cm[0,0] + cm[0,1] + cm[1,0] + cm[1,1])
accuracy