from database import Database
class Template(object):

    def __init__(self, name, filename, tags):
        self.name = name
        self.filename = filename
        self.tags = tags
        self.description = "Just another template."
        self.is_activated = True
        self.is_deleted = True
        self.origin_id = None
        self.versions = None
        self.db = Database()

    def set_description(self, new_description):
        self.description = new_description

    def save_to_db(self):
        self.db.create_template(self.name, self.filename, self.tags, self.description)

    def create_version(self):
        pass

    def get_version(self):
        pass

    def delete_version(self):
        pass
    
    def activate_version(self):
        pass
