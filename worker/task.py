from celery import Celery, Task 
from pymongo import MongoClient
import time

import config

import ml_templates

app = Celery('tasks')
app.config_from_object(config)

@app.task()
def add(x, y):
    time.sleep(5)
    return x + y

def runModel():
    print(ml_templates.train_model('./ml_templates/titanic_test.csv','./ml_templates/titanic_train.csv'))