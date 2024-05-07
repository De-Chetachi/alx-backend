#!/usr/bin/env python3
'''base caching'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''a basic cache class that inherits from BaseCaching
    BaseCaching implements a cache class
    with a max-itmes and cache_data field
    methods like print cache, get to retrieve a cacheitem based on key
    a put method to add data to the cache_data'''
    def __init__(self):
        '''initializer'''
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
