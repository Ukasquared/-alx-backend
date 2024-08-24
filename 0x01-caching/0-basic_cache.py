#!/usr/bin/env python3
"""caching module that works
as a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Base cache
    module"""

    def __init__(self):
        """initialise instance"""
        super().__init__()

    def put(self, key, item):
        """ add items to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get item from cache"""
        return self.cache_data.get(key)
