class Template(object):

    file_name = ""
    tags = []
    last_update = ""

    def __init__(self, name, tags):
        self.file_name = name
        self.tags = tags
