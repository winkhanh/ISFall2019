#!/usr/bin/env python3


class linearRegressionByMe:
    def __init__(self,accuracy):
        pass
        self.__accuracy=(1/2)**accuracy
        self.__coefficient=[]
        self.__numsOfCoeff=0
    def fit(self,data,target):
        self.data=data
        self.target=target
        if (len(data)!=0):
            self.__numsOfCoeff=len(data[0])+1
            self.__coefficient=[0]*self.__numsOfCoeff
        else:
            print("No data found")
        self.__chooseCoefficience(data,target)
    def predict(self,data):
        predict_target=[]
        for instance in data:
            result=0
            for i in range(self.__numsOfCoeff):
                if i!=(self.__numsOfCoeff-1):
                    result+=instance[i]*self.__coefficient[i]
                else:
                    result+=self.__coefficient[i]
            predict_target.append(result)
        return predict_target
    def score(self,testData,testTarget):
        res=self.__SSres(testData,testTarget)
        tot=self.__SStot(testTarget)
        
        return 1-res/tot
    def __SSres(self,data,target):
        ssRes=0
        predict_target=self.predict(data)
        for i in range( len(target) ):
            ssRes+=((target[i]-predict_target[i])**2)
        return ssRes
    def __SStot(self,target):
        ssTot=0
        meanTarget=0
        for instance in target:
            meanTarget+=float(instance)/(len(target))
        for instance in target:
            ssTot+= ((instance-meanTarget)**2)
        
        return ssTot
    def __chooseCoefficience(self,train_data,train_target):
        step=1.0
        meanTarget=0
        for instance in train_target:
            meanTarget+=float(instance)/(len(train_target))
        self.__coefficient[-1]=meanTarget
        currentSSRes=self.__SSres(train_data,train_target)
        flag=False
        while (step>self.__accuracy):
            flag=False
            for i in range(self.__numsOfCoeff):
                index=self.__numsOfCoeff-1-i
                self.__coefficient[index]-=step
                tempSSRes=self.__SSres(train_data,train_target)
                if (currentSSRes>tempSSRes) :
                    flag=True
                    currentSSRes=tempSSRes
                    break
                self.__coefficient[index]+=step*2
                tempSSRes=self.__SSres(train_data,train_target)
                if (currentSSRes>tempSSRes) :
                    flag=True
                    currentSSRes=tempSSRes
                    break
                self.__coefficient[index]-=step
            if (not flag):
                step/=2


