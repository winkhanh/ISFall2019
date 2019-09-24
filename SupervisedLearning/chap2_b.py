#!/usr/bin/env python3


from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from linearRegressionFromScratch import linearRegressionByMe
#import dataset
boston=datasets.load_boston()
X=boston.data
X_rooms = X[:,5]
X_rooms = X_rooms.reshape(-1,1)

y=boston.target

#split dataset
X_train, X_test, y_train, y_test= train_test_split(X_rooms,y,test_size=0.3,random_state=20)


reg_room=linear_model.LinearRegression()
reg_room.fit(X_train,y_train)
reg_roomScratch=linearRegressionByMe(30)
reg_roomScratch.fit(X_train,y_train)
y_pred = reg_room.predict(X_test)   
y_predScratch= reg_roomScratch.predict(X_test)
score=reg_room.score(X_test,y_test)
scoreScratch= reg_roomScratch.score(X_test,y_test)

print("SCORE:")
print(score)
print(scoreScratch)
print("##########################")
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.3,random_state=20)
reg_all=linear_model.LinearRegression()
reg_allScratch= linearRegressionByMe(30) #the highger accuracy is, the slower the program running
reg_all.fit(X_train,y_train)
reg_allScratch.fit(X_train,y_train)
y_pred = reg_all.predict(X_test)
score=reg_all.score(X_test,y_test)
scoreScratch=reg_allScratch.score(X_test,y_test)
print(score)
print(scoreScratch)