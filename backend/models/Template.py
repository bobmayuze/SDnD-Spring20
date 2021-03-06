"""
The model of the template
Stored in MongoDB as is
Contains metadata of the template, plus all the versions
"""

from . AbstractModel import AbstractModel
import json
from bson.objectid import ObjectId
from datetime import datetime
import copy 
from . Version import Version
class Template(AbstractModel):

    def __init__(self, name, filename, tags, description, json_payload = None):
        if json_payload:
            """
            Constructor for factory method.
            Since Python doesn't doesn't allow multiple constructors, we have to pass
            in an optional argument.
            """
            self.__dict__ = json.loads(json_payload)
            deserialized_versions = [] 
            for v in self.versions:
                deserialized_version = Version(None, None, None, json.dumps(v))
                deserialized_versions.append(deserialized_version)
            self.versions = deserialized_versions
        else:
            self.name = name
            self.filename = filename
            self.tags = tags
            self.description = description
            self.versions = []
            self.created_at = datetime.now()
            self.activated_version = None
            self.activated_name = name
            self.origin_id = None

    def add_version(self, version):
        """
        Add a version object to the versions array
        """
        for v in self.versions:
            v.is_activated = False
            pass
        self.versions.append(version)
        self.activated_version = str(version.version_id)
        self.activated_name = version.name
        return True

    def activate_version(self, version_id):
        """
        Activate a version given the version_id
        """
        for v in self.versions:
            v.is_activated = False

        for v in self.versions:
            if v.version_id == version_id:
                v.is_activated = True
                self.activated_version = version_id
                self.activated_name = v.name
                return True
        return False

    def delete_version(self, version_id):
        """
        Delete a version given the version_id
        """
        for v in self.versions:
            if v.version_id == version_id:
                v.is_deleted = True
                if v.version_id == self.activated_version and len(self.versions) > 0:
                    self.activated_version = self.origin_id
                    v.is_activated = False
                    self.versions[0].is_activated = True
                break
        return True

    def serialize(self):
        """
        Serialize the object for storing in MongoDB
        """
        clone = copy.copy(self)
        serialized_versions = []
        for v in clone.versions:
            serialized_versions.append(v.serialize())
        clone.versions = serialized_versions
        # clone._id = ObjectId(clone._id)
        return vars(clone) 
    
    @staticmethod
    def getTemplate(template_id):
        """
        Factory method for getting a template object given the JSON
        """
        from database import Database
        db = Database()
        t_json = db.get_single_template_by_id(template_id)
        return Template(None, None, None, None, t_json)
