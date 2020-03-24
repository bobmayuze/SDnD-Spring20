from . AbstractModel import AbstractModel
import json
from datetime import datetime
class Template(AbstractModel):

    def __init__(self, name, filename, tags, description):
        self.name = name
        self.filename = filename
        self.tags = tags
        self.description = description
        self.origin_id = None
        self.versions = []
        self.created_at = datetime.now()
        self.activated_version = None

    def add_version(self):
        pass

    def serialize(self):
        return vars(self) 
    
    def save_to_db(self):
        resp = self.db.create_template(self.name, self.filename, self.tags, self.description, self.origin_id)

