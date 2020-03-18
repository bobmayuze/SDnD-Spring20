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
        # print('TASK SUCCESS')
        # print('args',args)
        # print('kwargs', kwargs)
        self.db['jobs'].update_one(
            { 'task_id' : task_id },
            { '$set': { 'status' : 'SUCCESS' }}
        )

        template_origin_id = self.db['templates'].find_one({'_id' : ObjectId(args[0])})['origin_id']

        counter = self.db['regions'].find(
            {
                'name' : args[1],
                'templates' : {'$in' : [ObjectId(template_origin_id)]} 
            }
        )
        
        print("HAHA", counter.count())
        # Case 1 : This template is new to the region
        if counter.count() < 1:
            update_result = self.db['regions'].update_one(
                {'name' : args[1]},
                {
                    '$push': {
                        'templates': template_origin_id,
                        'deployment_task_ids' : task_id
                    }
                }
            )
            print('Updated', update_result.matched_count, 'region')            

        # Case 2 : This template has been deployed before
        if counter.count() >= 1:
            print('Update deployment_task_ids here')
            index_result = self.db['regions'].aggregate([ 
                { '$match': {"name":args[1]} },
                { "$project": { "matchedIndex": { "$indexOfArray": [ "$templates", template_origin_id ] } } } 
            ])
            deployment_task_index = 0
            for i in index_result:
                deployment_task_index = i['matchedIndex']
            self.db['regions'].update_one(
                {"name":args[1]},
                {
                    '$set' : {
                        'deployment_task_ids.' + str(deployment_task_index) : task_id
                    }
                }
            )
        
        
        # Case 2 : This template has been deployed before



    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.db['jobs'].update_one(
            { 'task_id' : task_id },
            { '$set': { 'status' : 'FAILED' }}
        )    



class CallbackTaskTest(Task):
    def __init__(self):
        self.db = MongoClient("mongodb://application_user:application_user_pass@mongo_result_backend:27017/?authSource=TMS_DB", connect=False)['TMS_DB']

    def on_success(self, retval, task_id, args, kwargs):
        # print('TASK SUCCESS')
        # print('args',args)
        # print('kwargs', kwargs)
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

@app.task(base=CallbackTaskTest)
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