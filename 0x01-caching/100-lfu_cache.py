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

        if key in self.cache_data:
            self.count[key] += 1
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_frequent_key = min(
                self.count.keys(), key=lambda k: self.count[k])
            self.cache_data.pop(least_frequent_key)
            self.count.pop(least_frequent_key)
            self.last.remove(least_frequent_key)
            print(f"DISCARD: {least_frequent_key}")

        self.cache_data[key] = item
        self.count[key] = 1
        self.last.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.count[key] += 1
        self.last.append(key)
        return self.cache_data[key]
