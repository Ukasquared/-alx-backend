#!/usr/bin/env python3
""" first in, first out """
basic_cache = __import__('0-basic_cache').BasicCache

class FIFOCache(basic_cache):
    """ first in first out"""
    def __init__(self):
        """calls parent constructor"""
        super().__init__()

    def put(self, key, item):
        """ adds to the cache"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item
        cache_list = list(self.cache_data.keys())
        cache_len = len(cache_list)
        if cache_len > self.MAX_ITEMS:
            print(f"DISCARD: {cache_list[0]}")
            delete = self.cache_data.pop(cache_list[0])
