from database import Database
class Template(object):

    def __init__(self, name, filename, tags):
        self.name = name
        self.filename = filename
        self.tags = tags
        self.description = "Just another template."
        self.is_activated = True
        self.is_deleted = False
        self.origin_id = None
        self.versions = None
        self.db = Database()

    def set_origin(self, origin_id):
        self.origin_id = origin_id
    
    def set_description(self, new_description):
        self.description = new_description

    def save_to_db(self):
        resp = self.db.create_template(self.name, self.filename, self.tags, self.description, self.origin_id)

