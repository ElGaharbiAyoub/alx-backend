#!/usr/bin/env python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache (BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.last = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                print("DISCARD: {}".format(self.last[0]))
                self.cache_data.pop(self.last[0])
                self.last.pop(0)
        self.cache_data[key] = item
        if key in self.last:
            self.last.remove(key)
        self.last.append(key)

    def get(self, key):
        """ get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.last:
            self.last.remove(key)
        self.last.append(key)
        return self.cache_data.get(key)
