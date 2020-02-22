from celery import Celery, Task 
from pymongo import MongoClient
import time

import config

import ml_templates

class CallbackTask(Task):
    def __init__(self):
        self.db = MongoClient("mongodb://application_user:application_user_pass@mongo_result_backend:27017/?authSource=scicatDB", connect=False)['scicatDB']

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


app = Celery('tasks')
app.config_from_object(config)

@app.task()
def add(x, y):
    time.sleep(5)
    return x + y

def runModel():
    print(ml_templates.train_model('./ml_templates/titanic_test.csv','./ml_templates/titanic_train.csv'))