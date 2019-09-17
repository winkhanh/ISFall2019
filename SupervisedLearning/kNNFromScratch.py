#!/usr/bin/env python3
class knnByMe:
    def __init__(self,k_neighbors=5):
        self.k_neighbors=k_neighbors
    def fit(self,data,target):
        self.data=data
        self.target=target
        self.accuracy=self.score(data,target)
    def score(self,testData,testTarget):
        sum=0
        correct=0
        predictTarget=self.predict(testData)
        for i in range(len(testData)):
            sum+=1
            if (predictTarget[i]==testTarget[i]):
                correct+=1
        return correct/sum
    def predict(self,data):
        predict_target=[]
        for instance in data:
            result=self.__vote(self.__chooseK(instance))
            predict_target.append(result)
        return predict_target
    def __distance(self,instance1, instance2):
        distance=0
        for i in range(len(instance1)):
            distance+=(instance1[i]-instance2[i])**2
        return distance
    def __chooseK(self,instance):
        tempList=[]
        counter=0
        for instanceX in self.data:
            tempList.append((self.__distance(instance,instanceX),counter))
            counter+=1
        tempList.sort(key=lambda pair: pair[0])
        chosen=[]
        for i in range (self.k_neighbors):
            chosen.append(tempList[i][1])
        return chosen
    def __vote(self,instanceIDList):
        voteRecord=dict()
        maxVote=0
        result=self.target[0]
        for idx in instanceIDList:
            aVote=self.target[idx]
            if aVote in voteRecord:
                voteRecord[aVote]=voteRecord[aVote]+1
            else:
                voteRecord[aVote]=1
            if (voteRecord[aVote]>maxVote):
                maxVote=voteRecord[aVote]
                result=aVote
        return result
    
