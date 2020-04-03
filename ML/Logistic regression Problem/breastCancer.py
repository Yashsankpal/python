import pandas as pa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as se

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

# train and test state 
from sklearn.model_selection import train_test_split

dataframe = pa.DataFrame(np.c_[data['data'],data['target']],columns = np.append(data['feature_names'],['target']))

X = dataframe.drop(['target'],axis=1)
y= dataframe['target']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=8)

#  Improving Training Model

min_train = X_train.min()
range_train = (X_train-min_train).max()
X_train_scaled = (X_train-min_train)/range_train

se.scatterplot(x=X_train_scaled['mean area'],y=X_train_scaled['mean smoothness'],hue=y_train)
plt.show()

min_test = X_test.min()
range_test = (X_test-min_test).max()
X_test_scaled = (X_test-min_test)/range_test

# Accuracy check 
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix

# more improved model

from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1, 1, 10, 100, 1000],'gamma': [1, 0.1, 0.01, 0.001, 0.0001],'kernel': ['rbf']}  

grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=4)
grid.fit(X_train_scaled,y_train)

print(grid.best_params_)

grid_prediction = grid.predict(X_test_scaled)

svc_model = SVC()

#svc_model.fit(X_train_scaled,y_train)

#y_predit = svc_model.predict(X_test_scaled)

cm = confusion_matrix(y_test,grid_prediction)

se.heatmap(cm,annot=True)
plt.show()

# accuracy percentage

print(classification_report(y_test,grid_prediction))


















""" 
#print(data.keys())
#for i in data.keys():
#    print(f'{i} : {data[i]}')
#print(data['data'].shape)

# data visulaization 
print(dataframe.head())
print(dataframe.tail())

print(se.pairplot(dataframe,hue='target',vars=['mean radius','mean texture','mean perimeter','mean area','mean smoothness']))
plt.show()

print(se.countplot(dataframe['target']))
plt.show()

plt.show()
plt.figure(figsize=(20,10))
se.heatmap(dataframe.corr(),annot=True)
plt.show()
"""