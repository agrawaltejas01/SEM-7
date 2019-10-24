"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

#Get default dataset
iris = datasets.load_iris()

#Convert into dataframe
x = pd.DataFrame(iris.data)
x.head()
#Name the columns
x.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width' ]
x.head()

#K-Mean clustering
a = KMeans(n_clusters = 3)
#Classify
a.fit(x)
#label the target
a.labels_

#plot graph
colormap = np.array(['Red', 'Green', 'Blue'])
z = plt.scatter(x.sepal_length, x.sepal_width, x.petal_length, c = colormap[a.labels_])

#accuracy
accuracy_score(iris.target, a.labels_)
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

data = pd.read_csv("/home/test/BE/CL-7_practice/ML/Datasets/Breast-cancer Dataset/breast-cancer-wisconsin.data", na_values = "?")
#breast_data = datasets.load_breast_cancer()
x = pd.DataFrame(data)
x.head() 
x.columns = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K']

x.isnull().sum()
x.fillna(0, inplace = True)
x.isna().sum()

plt.scatter(x.A,x.K )

a = KMeans(n_clusters=2)
a.fit(x)
a.labels_
colormap = np.array(['Red', 'Blue', 'Green'])
z = plt.scatter(x.A,x.H, c = colormap[a.labels_] )

accuracy_score(x.H, a.labels_, normalize=True)
"""
"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

data = datasets.load_wine()
x = pd.DataFrame(data.data)
x.head()
x.columns = ['alcohol', 'malic acid', 'ash', 'ash alcalinity',
                        'magnesium', 'total phenols', 'flavanoids',
                        'nonflavanoid phenols', 'proanthocyanins',
                        'color intensity', 'hue', 'OD280/OD315 of diluted wines',
                        'proline']

a = KMeans(n_clusters = 3)
a.fit(x)
a.labels_
colormap = np.array(['Red', 'Green', 'Blue'])

z = plt.scatter(x.alcohol, x.magnesium, x.hue, c = colormap[a.labels_])
"""

import pandas as pd
import numpy as np

from sklearn import datasets
data = datasets.load_iris()

iris = pd.DataFrame(data.data)
iris.columns = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']

from sklearn.cluster import KMeans
classifier = KMeans(n_clusters=3)
classifier.fit(iris)

classifier.labels_

colormap = np.array(['red', 'blue', 'green'])

import matplotlib.pyplot as plt

plt.scatter(iris.petal_length, iris.petal_width, c = colormap[classifier.labels_])

from sklearn.metrics import accuracy_score
acc = accuracy_score(data.target, classifier.labels_)
acc*100















