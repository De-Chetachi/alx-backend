#!/usr/bin/env python3
'''base caching'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''a basic cache class that inherits from BaseCaching
    BaseCaching implements a cache class
    with a max-itmes and cache_data field
    methods like print cache, get to retrieve a cacheitem based on key
    a put method to add data to the cache_data'''
    def __init__(self):
        '''initialize'''
        super().__init__()
        self.lfu = {}

    def put(self, key, item):
        '''adds to the cache_data
        if the items of cache data are more than 3
        removes the oldest item and add the new item'''

        if key and item:
            if key not in self.cache_data and len(
                    self.cache_data) > self.MAX_ITEMS - 1:
                min_freq = min(self.lfu.values())

                for key_, value_ in self.lfu.items():
                    if value_ == min_freq:
                        break
                del self.lfu[key_]
                del self.cache_data[key_]
                print(f"DISCARD: {key_}")
            if key in self.lfu:
                self.lfu[key] = self.lfu[key] + 1
            else:
                self.lfu[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        '''retrieves a cacheline fgiven the key'''
        try:
            if key in self.lfu:
                self.lfu[key] = self.lfu[key] + 1
            val = self.cache_data[key]
            return val
        except KeyError:
            return None
