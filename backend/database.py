import pymongo
from datetime import datetime
import json
from bson.objectid import ObjectId
import pandas as pd
class Database(object):
    '''
    Database CLass
    '''
    

    client = None

    # set client to be the mongodb
    def __init__(self):
        self.client = pymongo.MongoClient(
                "mongodb://application_user:application_user_pass@mongo_result_backend:27017/?authSource=TMS_DB",
            connect=False)

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

        df = pd.DataFrame(list(db.find(
            {"is_activated": True}
        )))
        if len(df) < 1:
            return json.dumps([])
        foo = df.sort_values('created_at', ascending=False).drop_duplicates(subset=['origin_id'])

        records = foo.to_dict('records')        

        # template_ids = db.distinct('origin_id',{})

        # temporarily just prints them all to stdout
        toReturn = []
        for record in records:
            # record = db.find_one({'_id': ObjectId(template_id)})
            print(record)
        #     # hacky way to fix the fact that the id is stored as an
        #     # ObjectID() object
            record['_id'] = str(record['_id'])
            record['origin_id'] = str(record['origin_id'])
            record['created_at'] = str(record['created_at'])
            # record['tags'] = list(record['tags'])
        #     # add it to the list to return
            toReturn.append(record)

        # # returns the pymongo cursor object
        return json.dumps(toReturn)

    def get_single_template_by_id(self, unique_id):
        db = self.client['TMS_DB']
        db = db['templates']

        record = db.find_one({'_id': ObjectId(unique_id)})
        record['_id'] = str(record['_id'])
        record['origin_id'] = str(record['origin_id'])
        record['created_at'] = str(record['created_at'])

        return json.dumps(record)

    def get_templates_by_keyword(self, keyword):
        db = self.client['TMS_DB']
        db = db['templates']
        ret_list = []
        print(keyword)
        for x in db.find({'tags': keyword}):
            ret_list.append(x)
            x['_id'] = str(x['_id'])
            x['origin_id'] = str(x['origin_id'])
            x['created_at'] = str(x['created_at'])
        return json.dumps(ret_list)

    def get_versions(self, origin_id):
        db = self.client['TMS_DB']
        db = db['templates']
        ret_list = []
        for x in db.find({'origin_id': ObjectId(origin_id)}):
            ret_list.append(x)
            x['_id'] = str(x['_id'])
            x['origin_id'] = str(x['origin_id'])
            x['created_at'] = str(x['created_at'])
        return json.dumps(ret_list)

    def activate_version(self, origin_id, version_id):
        db = self.client['TMS_DB']
        db = db['templates']
        db.update_many({
            'origin_id': ObjectId(origin_id)
            },{'$set': {
                'is_activated': False
            }})
        db.update_one({
            '_id': ObjectId(version_id) 
            },{'$set': {
                'is_activated': True
            }})
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

    def create_template(self, name, file_name, tags, description, origin_id = None):
        db = self.client['TMS_DB']
        db = db['templates']
        values = {}
        values['name'] = name
        values['file_name'] = file_name
        values['tags'] = tags
        values['description'] = description
        values['is_activated'] = True
        values['is_deleted'] = False
        values['created_at'] = datetime.now()
        if origin_id:
            test = db.update_many({
                        'origin_id': ObjectId(origin_id)
                    }, {'$set': {
                        'is_activated': False
                    }})
        create_result = db.insert_one(values)
        origin_id = create_result.inserted_id if not origin_id else origin_id
        print('Template', create_result.inserted_id, 'created')
        update_result = db.update_one(
                {
                    '_id': ObjectId(create_result.inserted_id)
                }, {'$set': {
                    'origin_id': ObjectId(origin_id)
                }})
        return update_result
