#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            first = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(first))
            self.cache_data.pop(first)
        self.cache_data[key] = item

    def get(self, key):
        """ get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
