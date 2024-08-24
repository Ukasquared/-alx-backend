#!/usr/bin/env python3
"""last in, first out cache"""
BaseCaching = __import__("base_caching").BaseCaching

class MRUCache(BaseCaching):
    """last in first out"""
    dequeue = []

    def __init__(self):
        """ calls the parent methods 
        and variables into eminent 
        class"""
        super().__init__()

    def put(self, key, item):
        """ add to the cache"""
        if key is None or item is None:
            pass
        if len(self.cache_data) < self.MAX_ITEMS:
            self.cache_data[key] = item
            self.dequeue.append(key)
        
        if key in self.dequeue:
            self.cache_data[key] = item
            self.dequeue.remove(key)
            self.dequeue.append(key)
        else:
            value = self.dequeue.pop(-1)
            self.cache_data.pop(value)
            print(f"DISCARD: {value}")
            self.dequeue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get the value from the cache"""
        if key in self.dequeue:
            self.dequeue.remove(key)
            self.dequeue.append(key)
        return self.cache_data.get(key)
