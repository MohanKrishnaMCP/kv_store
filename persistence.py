#implement persistence memory via file management
#periodically write in-memory data to file
#when server kv_store starts/restarts - load the file data to memory, so that data is not lost

import json
from kv_store import KeyValueStore

class PersistentKeyValueStore(KeyValueStore):
    def __init__(self, filename='db.json'):
        super().__init__()
        self.filename = filename
        self.load()
    
    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.store = json.load(f)
        except FileNotFoundError:
            self.store = {}
    
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.store, f)
    
    def setval(self, key, value):
        super().setval(key, value)
        self.save()
    
    def delete(self, key):
        super().delete(key)
        self.save()