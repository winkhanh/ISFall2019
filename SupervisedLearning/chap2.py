#!/usr/bin/env python3

from sklearn import datasets
import numpy as np 
from sklearn import linear_model
import matplotlib.pyplot as plt
boston=datasets.load_boston()

print(boston.keys())
print(boston.feature_names)
X=boston.data
y=boston.target
X_room=X[:,5]
print(X)
print("ROOM:")
print(X_room)

X_room=X_room.reshape(-1,1)
reg = linear_model.LinearRegression()

reg.fit(X_room, y)
prediction_space = np.linspace(min(X_room),max(X_room)).reshape(-1,1)
print("X")
plt.scatter(X_room,y,color="blue")
plt.plot(prediction_space,reg.predict(prediction_space),color='black',linewidth=3)
plt.show()