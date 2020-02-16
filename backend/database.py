import pymongo
from datetime import datetime
import json
from bson.objectid import ObjectId

class Database(object):

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
            {'is_activated' : True}
        )))

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
            record['key_words'] = list(record['key_words'])
        #     # add it to the list to return
            toReturn.append(record)

        # # returns the pymongo cursor object
        return json.dumps(toReturn)

