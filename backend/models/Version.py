from AbstractModel import AbstractModel
from Template import Template
class Version(Template):
    def __init__(self, name, filename, tags):
        self.is_activated = True
        self.is_deleted = False
        self.origin_id = None
        self.version_id = None

    def get_origin(self):
        return self.origin_id