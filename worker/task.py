from celery import Celery, Task 
from pymongo import MongoClient
from bson.objectid import ObjectId
import time

import config

import ml_templates

class CallbackTask(Task):
    def __init__(self):
        self.db = MongoClient("mongodb://application_user:application_user_pass@mongo_result_backend:27017/?authSource=TMS_DB", connect=False)['TMS_DB']
        
    def on_success(self, retval, task_id, args, kwargs):
        
        self.db['jobs'].update_one(
            { 'task_id' : task_id },
            { '$set': { 'status' : 'SUCCESS' }}
        )



    def on_failure(self, exc, task_id, args, kwargs, einfo):

        self.db['jobs'].update_one(
            { 'task_id' : task_id },
            { '$set': { 'status' : 'FAILED' }}
        )    


app = Celery('task')
app.config_from_object(config)

@app.task(base=CallbackTask)
def add(x, y):
    print(x)
    print(y)
    time.sleep(5)
    return str(x) + str(y)

@app.task()
def multiple(x, y):
    return x * y

@app.task(base=CallbackTask)
def big_task(x):
    print("Start ur {} seconds tasks.".format(x))
    time.sleep(int(x))
    print("Ending ur {} seconds tasks.".format(x))
    return 0

@app.task(base=CallbackTask)
def create_deployment(template_id, region_id):
    time.sleep(10)
    print("We will deploy template",template_id, "to reigon", region_id)
    return 0

def runModel():
    print(ml_templates.train_model('./ml_templates/titanic_test.csv','./ml_templates/titanic_train.csv'))