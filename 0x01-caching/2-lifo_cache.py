#!/usr/bin/env python3
"""last in, first out cache"""
BaseCaching = __import__("base_caching").BaseCaching

class LIFOCache(BaseCaching):
    """last in first out"""
    def __init__(self):
        """ calls the parent methods 
        and variables into eminent 
        class"""
        super().__init__()

    def put(self, key, item):
        """ add to the cache"""
        if key is None or item is None:
            pass
        if len(self.cache_data) < 4: 
            self.cache_data[key] = item
        else: 
            cache_list = list(self.cache_data.keys())
            if key in cache_list:
                self.cache_data.pop(key)
            else:
                print(f"DISCARD: {cache_list[-1]}")
                self.cache_data.popitem()
            self.cache_data[key] = item
