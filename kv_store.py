class KeyValueStore:

    def __init__(self):
        self.store = {}
    
    def setval(self, key, value):
        self.store[key] = value
        return True
    
    def get(self, key):
        return self.store.get(key, None)
    
    def delete(self, key):
        if key in self.store:
            del self.store[key]
            return True
        return False
    
    def exists(self, key):
        if key in self.store:
            return True
        return False
    
    def clear(self):
        self.store.clear()
        return True
    
    