#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in cahce data"""
        if key is None and item is Nane:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.queue.pop(0)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
