#!/usr/bin/env python3

#this chap is about the train/test split technique
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from kNNFromScratch import knnByMe
#import dataset
iris=datasets.load_iris()

X=iris.data 
y=iris.target
#split dataset

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=18, stratify=y)
#little explanation: stratify is the distribute sample. stratify=y means the distribution in 
#y_train and y_test reflect y



knn = KNeighborsClassifier(n_neighbors=8)
knnScratch=knnByMe(k_neighbors=5)
knn.fit(X_train,y_train)
knnScratch.fit(X_train,y_train)

y_pred = knn.predict(X_test)
y_predScratch=knnScratch.predict(X_test)

print(list(y_pred))
print(y_predScratch)
print(knn.score(X_test,y_test))
print(knnScratch.score(X_test,y_test))
