'''
Job Service
'''

import pymongo
from celery import Celery
from pymongo import MongoClient
import datetime
import json
from bson.objectid import ObjectId

import config


class deployment_job_service(object):
    '''
    Job Service for templates deployment jobs 
    '''

    def __init__(self):
        print('Job Service Created')
        self.app = Celery('tasks')
        self.app.config_from_object(config)
        self.mongo_db = MongoClient(
            "mongodb://application_user:application_user_pass@mongo_result_backend:27017/?authSource=TMS_DB"
        )['TMS_DB']
    
    # TODO: put pagination here https://www.codementor.io/arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr
    def get_jobs(self):
        '''
        Get list of jobs
        '''
        total_records = []
        cursor = self.mongo_db['jobs'].find().sort("create_time",
                                                   pymongo.DESCENDING)
        for record in cursor:
            # del record["_id"]
            record["_id"] = str(record["_id"])
            try:
                template_name = self.mongo_db['templates'].find_one({'_id' : ObjectId(record["task_name"]) })['name']
            except :
                template_name = "SOME TEMPLATE"
            
            record['template_name'] = template_name
            total_records.append(record)
        
        return total_records

    def create_deployment_job(self,
                              template_id,
                              region_id,
                              target_queue='sample_region_1'):
        '''
        Create a deployment job
        '''

        task = self.app.send_task(
            'task.add', [template_id, region_id],
            queue=target_queue)

        print('Created Task', task.id)

        self.mongo_db['jobs'].insert_one({
            'task_id': task.id,
            'task_name': template_id,
            'target_region': region_id,
            'create_time': datetime.datetime.now(),
            'status': 'PENDING'
        })

        return task

    def revoke_job(self, task_id):
        '''
        Revoke an ongoing job by task id in the db
        '''
        self.app.control.revoke(task_id, terminate=True)

        self.mongo_db['jobs'].update_one({
            'task_id': task_id
        }, {'$set': {
            'status': 'REVOKED'
        }})
        return ({'message': 'Job {} successfully revoked'.format(task_id)})

    def get_job_status(self, task_id):
        '''
        Get status of a deployment job
        '''
        return self.app.AsyncResult(task_id).status

    def get_job_detail(self, task_id):
        '''
        Get deployment job detail of a job
        '''
        result = self.mongo_db['jobs'].find_one({'task_id': task_id})

        del result['_id']
        return result
