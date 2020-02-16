#!/usr/bin/env python
# coding: utf-8

# In[1]:


# linear algebra
import numpy as np 
# data processing
import pandas as pd 
# Algorithms
from sklearn.linear_model import LogisticRegression


# In[2]:


test = pd.read_csv("titanic_test.csv")
train = pd.read_csv("titanic_train.csv")


# In[3]:


def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train[train["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age


# In[4]:


train["Age"] = train[["Age", "Pclass"]].apply(add_age,axis=1)


# In[5]:


train.drop("Cabin",inplace=True,axis=1)
train.dropna(inplace=True)


# In[6]:


sex = pd.get_dummies(train["Sex"],drop_first=True)
embarked = pd.get_dummies(train["Embarked"],drop_first=True)
pclass = pd.get_dummies(train["Pclass"],drop_first=True)


# In[7]:


train = pd.concat([train,pclass,sex,embarked],axis=1)
train.drop(["PassengerId","Pclass","Name","Sex","Ticket","Embarked"],axis=1,inplace=True)


# In[8]:


X = train.drop("Survived",axis=1)
y = train["Survived"]


# In[9]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)


# In[10]:


from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression(solver='newton-cg')
logmodel.fit(X_train,y_train)


# In[11]:


# predictions = logmodel.predict(X_test)
# from sklearn.metrics import classification_report
# print(classification_report(y_test, predictions))


# In[12]:


acc_log = round(logmodel.score(X_train, y_train) * 100, 2)


# In[13]:


print(acc_log)


# In[ ]:




