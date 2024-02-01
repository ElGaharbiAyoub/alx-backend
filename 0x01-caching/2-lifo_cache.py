#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                print("DISCARD: {}".format(self.last))
                self.cache_data.pop(self.last)
        self.cache_data[key] = item
        self.last = key

    def get(self, key):
        """ get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
