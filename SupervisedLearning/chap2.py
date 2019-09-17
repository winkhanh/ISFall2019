#!/usr/bin/env python3

#this chap is the first idea of how KNN works as well as how ML model in sklearn works
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()

X=iris.data 
y=iris.target

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X,y)

X_new=[
    [6.0, 4.9, 2.0, 3.0],
    [5.3, 2.5, 2.4, 2.0],
    [3.2, 2.5, 4.0, 1.0]
]

prediction=knn.predict(X_new)

print(prediction)