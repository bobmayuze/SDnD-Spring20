from celery import Celery, Task 
from pymongo import MongoClient
from bson.objectid import ObjectId
import time

import config

import ml_templates

# Tasks are the building blocks of Celery distributed computing

# This is the callback class for every task that is initiated, it contains code for tasks that succeed and tasks that fail
class CallbackTask(Task):
    # connecting to the database
    def __init__(self):
        self.db = MongoClient("mongodb://application_user:application_user_pass@mongo_result_backend:27017/?authSource=TMS_DB", connect=False)['TMS_DB']
    
    # code that will execute when tasks succeed
    def on_success(self, retval, task_id, args, kwargs):
        
        # update the jobs database to set the status to success
        self.db['jobs'].update_one(
            { 'task_id' : task_id },
            { '$set': { 'status' : 'SUCCESS' }}
        )
        # finding the template origin id
        template_origin_id = self.db['templates'].find_one({'_id' : ObjectId(args[0])})['origin_id']

        # counting the number of times the template id is in the regions database
        counter = self.db['regions'].find(
            {
                'name' : args[1],
                'templates' : {'$in' : [ObjectId(template_origin_id)]} 
            }
        )
        
        print("HAHA", counter.count())
        # Case 1 : This template is new to the region
        if counter.count() < 1:
            # updating the regions database with the necessary information
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


    # code that executes on failure
    def on_failure(self, exc, task_id, args, kwargs, einfo):

        self.db['jobs'].update_one(
            { 'task_id' : task_id },
            { '$set': { 'status' : 'FAILED' }}
        )    


app = Celery('task')
app.config_from_object(config)

# different callback functions for each task
@app.task(base=CallbackTask)
def add(x, y):
    print(x)
    print(y)
    time.sleep(5)
    return str(x) + str(y)

@app.task(base=CallbackTask)
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
    
# sample machine learning model function
@app.task(base=CallbackTask)
def runModel():
    print(ml_templates.train_model('./ml_templates/titanic_test.csv','./ml_templates/titanic_train.csv'))