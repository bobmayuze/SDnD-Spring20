"""
Model for a version
Contains metadata for a specific version
"""
from bson.objectid import ObjectId
import copy
import json
from . AbstractModel import AbstractModel
from datetime import datetime
class Version(AbstractModel):
    def __init__(self, name, filename, origin_id, json_payload = None):
        if json_payload:
            self.__dict__ = json.loads(json_payload)
        else:
            self.name = name 
            self.filename = filename
            self.is_activated = True
            self.is_deleted = False
            self.origin_id = str(origin_id)
            self.version_id = str(ObjectId())
            self.created_at = datetime.now()

    def get_origin(self):
        return self.origin_id

    def serialize(self):
        """
        Seralize a version for storing in DB
        """
        clone = copy.copy(self)
        clone.origin_id = ObjectId(clone.origin_id)
        clone.version_id = ObjectId(clone.version_id)
        return vars(self)

    @staticmethod
    def getVersion(template_id):
        """
        Factory method for getting a version. Not needed as of now
        """
        pass
