#!/usr/bin/env python3
"""LFU Caching"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.last = []
        self.count = {}

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
        if key not in self.count.keys():
            self.count[key] = 0
        self.count[key] += 1

    def get(self, key):
        """ get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.last:
            self.last.remove(key)
        self.last.append(key)
        if key not in self.count.keys():
            self.count[key] = 0
        self.count[key] += 1
        return self.cache_data.get(key)
