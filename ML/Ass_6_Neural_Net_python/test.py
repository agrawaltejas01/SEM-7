"""
import numpy as np
import pandas as pd

data = pd.read_csv("/home/test/BE/CL-7_practice/ML/Datasets/Diabetes Dataset/diabetes_csv.csv")
data['class'] = data['class'].replace("tested_negative", 0)
data['class'] = data['class'].replace("tested_positive", 1)

X = data.iloc[:,:8 ]
Y = data.iloc[:,8]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Neural network

import keras
from keras.models import Sequential
from keras.layers import Dense

def create_network():
    
    classifier = Sequential()
    
    #input layer will have 4 nodes
    #1st hidden layer will have 3 nodes
    classifier.add(Dense(4, activation='relu', input_dim = 8))    
    #2nd hidden layer will have 2 nodes
    classifier.add(Dense(4, activation='relu'))
    #3rd is output hence 1
    classifier.add(Dense(1, activation='relu'))
    
    #Compile whole NN
    classifier.compile(optimizer = 'adam', loss ='binary_crossentropy' , metrics =['accuracy'] )
    
    return classifier

classifier = create_network()
classifier.fit(X_train, Y_train, batch_size=25, epochs=500)

Y_pred = classifier.predict(X_test)
Y_pred = (Y_pred>0.5)

from sklearn.metrics import accuracy_score, confusion_matrix
acc = accuracy_score(Y_test, Y_pred)
acc

cm = confusion_matrix(Y_test, Y_pred)
cm

import graphviz
from ann_visualizer.visualize import ann_viz


"""
"""
import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
data = load_boston()

X = data.data
Y = data.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)  

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) 

import keras
from keras.models import Sequential
from keras.layers import Dense

def create_network():
    
    classifier = Sequential()
    
    classifier.add(Dense(64, activation='relu', input_dim = 13))
    classifier.add(Dense(64, activation='relu'))    
    classifier.add(Dense(1,activation='relu'))
    
    classifier.compile(optimizer = 'adam', loss = 'mse', metrics = ['accuracy'])
    
    return classifier

classifier = create_network()
classifier.fit(X_train, Y_train, batch_size = 25, epochs=500)
Y_pred = classifier.predict(X_test)

score = classifier.evaluate(X_test, Y_test)
score

import graphviz
from ann_visualizer.visualize import ann_viz
ann_viz(classifier)
"""

import numpy as np
import pandas as pd
import sklearn.datasets as datasets

data = datasets.load_wine()

X = data.data
Y = data.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

import keras
from keras.models import Sequential
from keras.layers import Dense

def create_network():
    
    classifier = Sequential()
    
    classifier.add(Dense(20,activation='relu', input_dim = 13))
    classifier.add(Dense(8, activation='relu'))
    classifier.add(Dense(4, activation='relu'))
    classifier.add(Dense(1, activation = 'relu'))
    
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    return classifier

classifier= create_network()
classifier.fit(X_train, Y_train, epochs=500, batch_size = 25)
Y_pred = classifier.predict(X_test)

import graphviz
from ann_visualizer.visualize import ann_viz

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
cm

score = classifier.evaluate(X_test, Y_test)
score

ann_viz(classifier)



