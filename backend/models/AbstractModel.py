from abc import ABC, abstractmethod
import database
class AbstractModel(ABC):
    def __init__(self):
        self.db = database.getDB()

    @abstractmethod
    def serialize(self):
        pass