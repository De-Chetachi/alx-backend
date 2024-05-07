#!/usr/bin/env python3
'''base caching'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''a basic cache class that inherits from BaseCaching
    BaseCaching implements a cache class
    with a max-itmes and cache_data field
    methods like print cache, get to retrieve a cacheitem based on key
    a put method to add data to the cache_data'''
    def __init__(self):
        '''initialize'''
        super().__init__()

    def put(self, key, item):
        '''adds to the cache_data
        if the items of cache data are more than 3
        removes the oldest item and add the new item'''

        if key and item:
            if key not in self.cache_data and len(
                    self.cache_data) > self.MAX_ITEMS - 1:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item

    def get(self, key):
        '''retrieves a cacheline fgiven the key'''
        try:
            return self.cache_data[key]
        except KeyError:
            return None
