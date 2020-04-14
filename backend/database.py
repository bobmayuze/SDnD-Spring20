import pymongo
from datetime import datetime
import json
from bson.objectid import ObjectId
import pandas as pd

from models import Template
class Database(object):
    '''
    Database CLass
    '''
    instance = None
    @staticmethod
    def getDB():
        if Database.instance == None:
            Database()
        return Database.instance

    client = None

    # set client to be the mongodb
    def __init__(self):
        self.client = pymongo.MongoClient(
                "mongodb://application_user:application_user_pass@mongo_result_backend:27017/?authSource=TMS_DB",
            connect=False)
        Database.instance = self

    '''
    fetches all regions from the collections named regions

    '''

    def get_regions(self):
        db = self.client['TMS_DB']
        db = db['regions']
        docs = db.find({})
        toReturn = []
        for doc in docs:

            doc['_id'] = str(doc['_id'])

            toReturn.append(doc)

        return json.dumps(toReturn)

    def get_templates(self):
        db = self.client['TMS_DB']
        db = db['templates']

        templates = db.find({}, {'versions': 0})
        toReturn = []
        for template in list(templates):
            template['activated_version'] = str(template['activated_version'])
            template['origin_id'] = str(template['origin_id'])
            template['_id'] = str(template['_id'])
            template['created_at'] = str(template['created_at'])
            toReturn.append(template)
        return json.dumps(toReturn)

    def get_single_template_by_id(self, unique_id, regions_required = False):
        db = self.client['TMS_DB']
        db = db['templates']
        record = db.find_one({'_id': ObjectId(unique_id)})
        record['_id'] = str(record['_id'])
        record['activated_version'] = str(record['activated_version'])
        record['origin_id'] = str(record['origin_id'])
        record['created_at'] = str(record['created_at'])
        serialized_versions = []
        for v in record['versions']:
            v['version_id'] = str(v['version_id'])
            v['origin_id'] = str(v['origin_id'])
            v['created_at'] = str(v['created_at'])
            serialized_versions.append(v)
        record['versions'] = serialized_versions
        if regions_required:
            db = self.client['TMS_DB']
            db = db['regions']
            regions = db.find({"templates": ObjectId(unique_id)})
            region_list = []
            for region in regions:
               region_list.append(region['name']) 
            record['regions'] = region_list

        return json.dumps(record)

    def get_templates_by_keyword(self, keyword):
        db = self.client['TMS_DB']
        db = db['templates']
        ret_list = []
        docs = db.find({
            'name': {'$regex': keyword}
        })
        for x in docs:
            x['_id'] = str(x['_id'])
            x['origin_id'] = str(x['origin_id'])
            x['versions'] = None
            x['activated_version'] = str(x['activated_version'])
            x['created_at'] = str(x['created_at'])
            ret_list.append(x)

        return json.dumps(ret_list)

    def get_versions(self, origin_id):
        db = self.client['TMS_DB']
        db = db['templates']
        query = db.find(
            {'_id': ObjectId(origin_id)}, 
            {'_id': 0, 'versions': 1}
        )
        ret_list = []
        for result in query:
            for version in result['versions']:
                if version['is_deleted']:
                    continue
                version['origin_id'] = str(version['origin_id'])
                version['version_id'] = str(version['version_id'])
                version['created_at'] = str(version['created_at'])
                ret_list.append(version)
        return json.dumps(ret_list) 

    def activate_version(self, origin_id, version_id):
        db = self.client['TMS_DB']
        db = db['templates']
        db.update({ 
            "_id": ObjectId(origin_id), 
            "versions.is_activated": True},
           {"$set": {"versions.$.is_activated": False}}
        )
        db.update({
            "_id": ObjectId(origin_id), 
            "versions.version_id": version_id},
           {"$set": {"versions.$.is_activated": True}}
        )
        db.update({"_id": ObjectId(origin_id)}, {"$set": {"activated_version": ObjectId(version_id)}}) # serialize?
        return json.dumps({"message": "update succesful"})

    def delete_version(self, origin_id, version_id):
        db = self.client['TMS_DB']
        db = db['templates']
        target = db.find_one({
            '_id': ObjectId(version_id)
        })
        if target and target['is_activated'] == True:
            db.update_one({
                '_id': ObjectId(origin_id) 
            },{'$set': {
                    'is_activated': True
            }})
        db.delete_one({
            '_id': ObjectId(version_id)
        })
        return json.dumps({"message": "deletion succesful"})


    def update_template(self, template):
        db = self.client['TMS_DB']
        db = db['templates']
        del(template._id)
        db.replace_one(
            { '_id': ObjectId(template.origin_id) },
            template.serialize()
        )
        return True

    def create_template(self, template, filename = None):
        # Version shouldn't be created here, but for now I'm going to do it.
        db = self.client['TMS_DB']
        db = db['templates']
        create_result = db.insert_one(template.serialize())
        origin_id = create_result.inserted_id
        new_version = {
            "name": template.name,
            "filename": filename,
            "is_activated": True,
            "is_deleted": False,
            "origin_id": ObjectId(create_result.inserted_id),
            "version_id": ObjectId(create_result.inserted_id),
            "created_at": datetime.now()
        }
        resp = db.update_one(
            {
                '_id': ObjectId(create_result.inserted_id)
            }, 
            {
                '$set': {
                    'activated_version': ObjectId(origin_id),
                    'origin_id': ObjectId(origin_id) 
                },
                '$push': {
                    'versions': new_version
                }
            }
        )
        return {"msg": "template created succesfully"}
 
    def create_region(self, name):
        # TODO Check if a region exist or if u should drop it
        db = self.client['TMS_DB']

        db = db['regions']

            ## Delete duplicate values
        if (db.find_one({ 'name': name })):
        
            db.delete_many({ 'name': name})
        
        values = {}
        values['deployment_task_ids'] = []
        values['templates'] = []
        values['name'] = name

        ret = db.insert_one(values)
        return ret