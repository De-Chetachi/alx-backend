#!/usr/bin/env python3
'''base caching'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''a basic cache class that inherits from BaseCaching
    BaseCaching implements a cache class
    with a max-itmes and cache_data field
    methods like print cache, get to retrieve a cacheitem based on key
    a put method to add data to the cache_data'''
    def __init__(self):
        '''initialize'''
        super().__init__()
        self.lru = {}
        self.index = 0

    def put(self, key, item):
        '''adds to the cache_data
        if the items of cache data are more than 3
        removes the oldest item and add the new item'''

        if key and item:
            if key not in self.cache_data and len(
                    self.cache_data) > self.MAX_ITEMS - 1:
                del_key = self.lru[min(self.lru)]
                del self.lru[min(self.lru)]
                del self.cache_data[del_key]
                print(f"DISCARD: {del_key}")
            for key_, value_ in self.lru.items():
                if value_ == key:
                    del self.lru[key_]
                    break
            self.lru[self.index] = key
            self.index += 1
            self.cache_data[key] = item

    def get(self, key):
        '''retrieves a cacheline fgiven the key'''
        try:
            for key_, value_ in self.lru.items():
                if value_ == key:
                    del self.lru[key_]
                    break
            val = self.cache_data[key]
            if val:
                self.lru[self.index] = key
                self.index += 1
            return val
        except KeyError:
            return None
