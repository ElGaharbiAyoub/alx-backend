#!/usr/bin/env python3
"""LFU Caching"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.count = {}
    
        def put(self, key, item):
            """ Add an item in the cache"""
            if key is None or item is None:
                return
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    min_value = min(self.count.values())
                    min_keys = [k for k in self.count if self.count[k] == min_value]
                    if len(min_keys) == 1:
                        print("DISCARD: {}".format(min_keys[0]))
                        self.cache_data.pop(min_keys[0])
                        self.count.pop(min_keys[0])
                    else:
                        for k in self.last:
                            if k in min_keys:
                                print("DISCARD: {}".format(k))
                                self.cache_data.pop(k)
                                self.count.pop(k)
                                break
            self.cache_data[key] = item
            if key in self.count.keys():
                self.count[key] += 1
            else:
                self.count[key] = 1
    
        def get(self, key):
            """ get an item by key"""
            if key is None or key not in self.cache_data.keys():
                return None
            self.count[key] += 1
            return self.cache_data.get(key)
