"""import numpy as np
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

from matplotlib.colors import ListedColormap
x_set, y_set = X_test, Y_test
X1 , X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
                      np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)

plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.title("SVM")
plt.show()"""

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import data
data = pd.read_csv("/home/test/BE/CL-7_practice/ML/Ass_5_SVM_python/diabetes_csv.csv")  
data['class'].replace("tested_negative", 0, inplace = True)
data['class'].replace("tested_positive", 1, inplace = True)
data['class']

X = data.iloc[:, [6,7]].values
Y = data.iloc[:, 8].values

#Split dataset
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.25, random_state = 0)
 
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
Y_pred = classifier.predict(X_test)

#Confussion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
cm
accuracy = (cm[0,0]+cm[1,1]) / (cm[0,0] + cm[0,1] + cm[1,0] + cm[1,1])
accuracy

#Plot
X_set, Y_set = X_test, Y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() -1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() -1, stop = X_set[:, 1].max() + 1, step = 0.01))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i,j in enumerate(np.unique(Y_set)):
   plt.scatter(X_set[Y_set == j,0], X_set[Y_set == j,1],
               c = ListedColormap(('red', 'green'))(i), label = j)

plt.title('SVM Diabetes')
plt.xlabel('prdei')
plt.ylabel('age')
plt.show()

"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

#import
data = pd.read_csv("/home/test/BE/CL-7_practice/ML/Datasets/Wine Dataset/wine.data", sep = ",")
X = data.iloc[:, 1:].values
Y = data.iloc[:, 0].values

#Split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

#plt.scatter(X[1],X[2], X[0])

#Scale
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#SVM
from sklearn.svm import SVC
classifier = SVC(kernel = "sigmoid", random_state = 0)
classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_test)

#Confussion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)
cm

acc = cm[0,0] + cm[1,1] + cm[2,2]/  cm.sum()
acc

X_set, Y_set = X_test, Y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() -1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() -1, stop = X_set[:, 1].max() + 1, step = 0.01))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i,j in enumerate(np.unique(Y_set)):
   plt.scatter(X_set[Y_set == j,0], X_set[Y_set == j,1],
               c = ListedColormap(('red', 'green', 'blue'))(i), label = j)
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

data = datasets.load_boston().data
data = pd.DataFrame(data)
X = data.iloc[:, [0,1,2,3,4,5,6,7,9,10,11,12]].values
Y = data.iloc[:,8].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
classifier = SVC(kernel = "linear", random_state = 0)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
cm

acc = 0
for i in range(len(cm)):
    acc = acc + cm[i,i]
acc = acc / cm.sum()
acc

from matplotlib.colors import ListedColormap
X_set, Y_Set = X_test, Y_test
X1 , X2 = np.meshgrid(np.arange(start = X_set[:,0].min() - 1, stop = X_set[:,0].max() + 1, step = 0.01),
                      np.arange(start = X_set[:,1].min() - 1, stop = X_set[:,1].max() + 1, step = 0.01))

for i,j in enumerate(np.unique(Y_Set)):
   plt.scatter(X_set[Y_Set == j,0], X_set[Y_Set == j,1],
               c = ListedColormap(('red', 'green', 'blue', 'yellow', 'orange'))(i), label = j)
   """
   
import numpy as np
import pandas as pd

data = pd.read_csv("/home/test/BE/CL-7_practice/ML/Ass_5_SVM_python/diabetes_csv.csv")
data['class'] = data['class'].replace('tested_negative', 0)
data['class'] = data['class'].replace('tested_positive', 1)

X = data.iloc[:, 0:8]
Y = data.iloc[:,8]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0) 

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
classifier = SVC(kernel = "linear")
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
cm

acc = (cm[0,0] + cm[1,1])/cm.sum()
acc

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

X_set, Y_set = X_test, Y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min() - 1, stop = X_set[:,0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:,1].min() - 1, stop = X_set[:,1].max() + 1, step = 0.01))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i,j in enumerate(np.unique(Y_set)):
    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.xlabel('predi')
plt.ylabel('age')
plt.title('Diabetes')
    