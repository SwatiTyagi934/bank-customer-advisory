import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from modelfunctions import applyall
import pickle
import numpy as np
dataset=pd.read_csv("original.csv", header=0,delimiter=",")
data=dataset[['age', 'job','marital','education','default','balance','housing','loan','riskclassification']]
def updatebalance(x):
    x = x*100
    return float(x)
df=data
df.balance=df.balance.apply(updatebalance)
df=applyall(df)

x=df[['age', 'job','marital','education','default','balance','housing','loan']]
y=df['riskclassification']
train_x,test_x,train_y,test_y=train_test_split(x,y,train_size=0.8, test_size=0.2)

def train_model(classifier,feature,label,feature_valid,label_valid):
    classifier.fit(feature,label)
    predictions=classifier.predict(feature_valid)
    return metrics.accuracy_score(predictions,label_valid)

accuracy=train_model(RandomForestClassifier(),train_x,train_y,test_x,test_y)
print(accuracy)

model = RandomForestClassifier()
model.fit(x,y)
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
print("writing model")